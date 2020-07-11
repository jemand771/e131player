import time

import sacn

from player import Player
from queuecommand import QueueCommand


def main():

    p = Player()
    p.load_config()
    p.register_devices()
    p.set_pixels("door", list(range(0, 10)), [[255, 0, 0], [0, 0, 255]])
    p.start()
    # todo color generators
    # todo think about REST commands
    # flask / rest api


if __name__ == "__main__":
    main()
