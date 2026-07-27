const map = L.map("map").setView([50.45, 30.52], 11);

L.tileLayer(
"https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
{
    attribution: "OpenStreetMap"
}
).addTo(map);

fetch("/api/zones")
.then(r => r.json())
.then(data => {

    L.geoJSON(data, {

        onEachFeature(feature, layer){

            layer.bindPopup(
                feature.properties.name
            );

        }

    }).addTo(map);

});
