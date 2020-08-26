import colorsys
import time

import config
from queuecommand import QueueCommand


class Effect:

    def __init__(self, *args, **kwargs):
        self.duration = 5
        self.speed = 1
        self.sspeed = 1
        self.color = (0, 25, 25)
        for x in ("duration", "speed", "color", "sspped"):
            if x in kwargs:
                exec("self." + x + " = " + str(kwargs[x]))

    def get_commands(self, device, pixels, starttime):
        lst = self.get_commands_universal()
        for cmd in lst:
            cmd.set_details(starttime, device, pixels)
        return lst

    def get_commands_universal(self):
        return []  # implemented by effect class

    @staticmethod
    def hsv2rgb(h, s, v):
        return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h / 255, s / 255, v / 255))


class RainbowEffect(Effect):

    def get_commands_universal(self):
        rainbow_loop = [self.hsv2rgb(x, 255, 255) for x in range(255)]
        cmds = []
        for x in range(self.duration * config.tps * self.speed):
            cmd = QueueCommand(x / config.tps / self.speed, "set_pixels", colors=rainbow_loop)
            # todo speeds slower than 1
            rainbow_loop = rainbow_loop[self.sspeed:] + rainbow_loop[0:self.sspeed]
            cmds.append(cmd)
        return cmds
