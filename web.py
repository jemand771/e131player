from flask import Flask

from player import Player

app = Flask(__name__)


@app.route("/stop")
def stop_server():
    p.stop()
    return "server stopped"


def queue_scipt(device, script):
    p.push()


if __name__ == "__main__":
    p = Player()
    p.load_config()
    p.register_devices()
    p.start()
    app.run(host="0.0.0.0", port=5000)
