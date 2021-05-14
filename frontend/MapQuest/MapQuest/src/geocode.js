// change user input into latitude and longitude cordinates through Geocoding API provided by MapQuest
var script = document.createElement('script');
script.src = 'getapidata.js';         
document.head.appendChild(script)

var ax = document.createElement('ax');
ax.src='https://unpkg.com/axios/dist/axios.min.js';
document.head.appendChild(ax);

const geocode_url = "http://www.mapquestapi.com/geocoding/v1/address";

function getLatLon(startLoc, destLoc) {
    var startLat, startLon, endLat, endLon;
    axios.get(geocode_url, {
        params: {
            key: 'ObOOcgLBayNvuhkFMUAKvmh5y7pXteON',
            location: startLoc
        }
    })
    .then(function(response) {
        console.log(response);
        // save starting location's latitude and longitude cordinates
        startLat = response.data.results[0].locations[0].latLng.lat;
        startLon = response.data.results[0].locations[0].latLng.lng;
    })
    .catch(function(error) {
        console.log(error);
        alert("Please Enter a Valid Address");
    });

    axios.get(geocode_url, {
        params: {
            key: 'ObOOcgLBayNvuhkFMUAKvmh5y7pXteON',
            location: destLoc
        }
    })
    .then(function(response) {
        console.log(response);
        // save destinations latitude and longitude cordinates
        endLat = response.data.results[0].locations[0].latLng.lat;
        endLon = response.data.results[0].locations[0].latLng.lng;
    })
    .then(function(response) {
        var startCord = [startLat, startLon];
        var endCord = [endLat, endLon];
        console.log("starting cords: " + startCord);
        console.log("destination cords: " + endCord);
        getData(startLat, startLon, endLat, endLon);
    })
    .catch(function(error) {
        console.log(error);
        alert("Please Enter A Valid Address");
    });
}