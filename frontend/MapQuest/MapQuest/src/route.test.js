var srcLat = 41.510853;
var srcLon = -81.602861;
var desLat = 41.411359;
var desLon = -81.837581;

//const getData = require("./getapidata.js");

// var api = document.createElement('api');
// api.scr='getapidata.js';
// document.head.appendChild(api);

// get data from local RESTful API
var route = document.createElement('route');
route.scr='route.js';
document.head.appendChild(route);

var average = document.createElement('average');
average.scr='index.html';
document.head.appendChild(average);

var table = document.createElement('table');
table.scr='index.html';
document.head.appendChild(table);

var ax = document.createElement('ax');
ax.src='https://unpkg.com/axios/dist/axios.min.js';
document.head.appendChild(ax);

const axios = require('axios');

const api_url = 'http://127.0.0.1:5000/';
function getData(sLat, sLon, eLat, eLon) {
    axios.get(api_url, {
        params: {
            srclat: sLat,
            srclon: sLon,
            destlat: eLat,
            destlon: eLon
        }
    })
    .then(function(response){
        console.log(response);
        test("Returns 41.51083,-81.602837 for given start lat and lon cordinates", () => {
            var maneuverLat = response.data.path.legs[0].maneuvers[0].startPoint.lat;
            var maneuverLon = response.data.path.legs[0].maneuvers[0].startPoint.lng;
            var maneuverCord = [maneuverLat, maneuverLon];
            expect(maneuverCord).toBe(41.51083,-81.602837);
        });
    })
    .catch(function(error) {
        console.log(error);
    })
}

getData(srcLat, srcLon, desLat, desLon);