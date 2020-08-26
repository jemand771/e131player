class QueueCommand:

    def __init__(self, time, cmd, *args, **kwargs):
        self.time = time
        self.cmd = cmd
        self.args = args
        self.kwargs = kwargs
        pass

    def set_details(self, starttime, device, pixels):
        self.time += starttime
        self.kwargs["pixels"] = pixels
        self.kwargs["device"] = device

    def __repr__(self):
        return "<QueueCommand time " + str(self.time) + ">"
