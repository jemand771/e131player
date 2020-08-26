import json
import math
import threading
import time

import sacn

from queuecommand import QueueCommand


class Player:

    def __init__(self):
        self.sender = sacn.sACNsender()
        self.sender.start(bind_address="0.0.0.0")
        self.queue = []
        self.devices = {}
        self.thread_running = True
        self.thread = threading.Thread(target=self.process_queue_loop, args=(0.05,))

    def load_config(self):

        # todo config folder
        with open("devices.json") as f:
            devices = json.load(f)
        # todo universe type (simple vs custom/advanced)
        for dev in devices:
            d = {
                "display_name": dev["display_name"],
                "universe": dev["universe"],
                "pixels": dev["pixels"]
            }
            self.devices[dev["name"]] = d

    def register_devices(self):

        for name, d in self.devices.items():
            num_universes = math.ceil(d["pixels"] / 170)
            for un in range(num_universes):
                u = un + d["universe"]
                self.sender.activate_output(u)
                self.sender[u].multicast = True

    def set_pixel(self, device, pixel, color):

        universe, pixel = self.pixel_to_universe(device, pixel)
        dmx = list(self.sender[universe].dmx_data)
        dmx[pixel:pixel+3] = color
        self.sender[universe].dmx_data = dmx

    def set_pixels(self, device, pixels, colors):
        numcols = len(colors)
        pixels = sorted([self.pixel_to_universe(device, p) for p in pixels], key=lambda k: k[0])
        dmx = {}
        for i, (universe, pixel) in enumerate(pixels):
            if not universe in dmx:
                dmx[universe] = list(self.sender[universe].dmx_data)
            color = colors[i % numcols]
            dmx[universe][pixel:pixel+3] = color
        for u, data in dmx.items():
            self.sender[u].dmx_data = data


    def pixel_to_universe(self, device, pixel):
        if type(device) == str:
            device = self.devices[device]
        universe = device["universe"] + math.floor(device["pixels"] / 170) - 1
        pixel %= 170
        pixel *= 3
        return universe, pixel

    def push(self, cmd):

        if type(cmd) == QueueCommand:
            self.queue.append(cmd)
        else:
            self.queue.extend(cmd)
        self.queue = sorted(self.queue, key=lambda k: k.time)

    def push_effect(self, eff):
        # todo parse an effect class -> iterate queue-adding
        pass

    def process_queue(self):

        while True:
            if len(self.queue) == 0:
                break
            elem = self.queue[0]
            if elem.time > time.time():
                break
            # todo better command classes ?
            if elem.cmd == "set_pixel":
                self.set_pixel(*elem.args, **elem.kwargs)
            del self.queue[0]

    def process_queue_loop(self, delay):
        while self.thread_running:
            self.process_queue()
            time.sleep(delay)

    def start(self):
        self.thread_running = True
        self.thread.start()

    def stop(self):
        self.thread_running = False