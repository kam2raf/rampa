import json

FILE = "data/no_fly_zones.geojson"

def load_geojson():

    with open(FILE, encoding="utf8") as f:
        return json.load(f)
