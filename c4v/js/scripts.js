$(document).ready( () => {
  console.log("Ready!");

// Load the tile images from OpenStreetMap
var mytiles = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
});
// Initialise an empty map
var map = L.map('map');
// Read the GeoJSON data with jQuery, and create a circleMarker element for each tweet
// Each tweet will be represented by a nice red dot
$.getJSON("./geo_data.json", function(data) {
  // debugger;
    var myStyle = {
        radius: 8,
        fillColor: "red",
        color: "red",
        weight: 1,
        opacity: 1,
        fillOpacity: 1
    };

    var geojson = L.geoJSON(data, {
        pointToLayer: function (feature, latlng) {
            return L.circleMarker(latlng, myStyle);
        }
    });
    // geojson.coordsToLatLng();
    geojson.addTo(map);
});
// Add the tiles to the map, and initialise the view in the middle of Europe

map.addLayer(mytiles).setView([7.996932, -65.948423], 6);



});
