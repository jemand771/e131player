from flask import Flask, request

from player import Player

app = Flask(__name__)
p = Player()


@app.route("/stop")
def stop_server():
    p.stop()
    return "server stopped"


def start_server():
    p.load_config()
    p.register_devices()
    p.start()
    app.run(host="0.0.0.0", port=5000)


@app.route("/<device>/solid")
def solid_color(device):
    color = request.args.get('color')
    color = list(int(color[i:i + 2], 16) for i in (0, 2, 4))
    dev = p.devices[device]
    p.set_pixels(device, range(dev["pixels"]), [color])
    return str(color)


if __name__ == "__main__":
    start_server()

