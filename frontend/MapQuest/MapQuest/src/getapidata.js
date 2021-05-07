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

//const axios = require('axios');

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
        return response;
    })
    .then(function(response){
        routing(response);
        buildAboveAverage(response);
        buildTable(response);
    })
    .catch(function(error) {
        console.log(error);
        alert(error);
    })
}
// module.exports = getData;