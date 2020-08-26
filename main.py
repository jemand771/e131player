import time

import sacn

import effects
from player import Player
from queuecommand import QueueCommand


def main():

    p = Player()
    p.load_config()
    p.register_devices()
    rb = effects.RainbowEffect(duration=5, speed=1)
    p.push_effect(rb, "test")
    #p.set_pixels("door", list(range(20)), [[255, 0, 0], [0, 0, 255]])
    p.start()

    # todo color generators
    # todo think about REST commands
    # flask / rest api


if __name__ == "__main__":
    main()
