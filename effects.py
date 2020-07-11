from queuecommand import QueueCommand

class Effect:

    def __init__(self, *args, **kwargs):
        for x in ("duration", "speed", "color"):
            if x in kwargs:
                exec("self." + x + " = " + str(kwargs[x]))

    def get_commands(self):
        pass


class RainbowEffect(Effect):

    def get_commands(self):
        rainbow_loop = [[255, 0, 0], [255, 0, 255], [0, 0, 255], [255, 0, 255]]
        # todo how to put time+device into command *dynamically* (regardless of device)
        return [QueueCommand()]