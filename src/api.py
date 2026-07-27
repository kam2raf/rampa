from flask import jsonify
from loader import load_geojson

def register_api(app):

    @app.route("/api/zones")
    def zones():
        return jsonify(load_geojson())
