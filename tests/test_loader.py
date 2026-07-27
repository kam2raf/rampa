from src.loader import load_geojson

def test_geojson():

    data = load_geojson()

    assert data["type"] == "FeatureCollection"
