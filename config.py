import json

# NOTE: config values should not be changed during runtime as things might break.
# just restart the program after making changes to config.json
with open("config/config.json") as f:
    js = json.load(f)
    tps = js.get("tps", 20)
    mspt = 1 / tps
    bind_address = js.get("bind_address", "0.0.0.0")
