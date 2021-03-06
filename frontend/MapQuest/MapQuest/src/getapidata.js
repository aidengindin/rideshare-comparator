// get data from local RESTful API
// var route = document.createElement('route');
// route.scr='route.js';
// document.head.appendChild(route);

// var average = document.createElement('average');
// average.scr='index.html';
// document.head.appendChild(average);

// var table = document.createElement('table');
// table.scr='index.html';
// document.head.appendChild(table);

var ax = document.createElement('ax');
ax.src='https://unpkg.com/axios/dist/axios.min.js';
document.head.appendChild(ax);

const axios = require('axios');
//import axios from 'axios';

const api_url = 'http://127.0.0.1:5000/';
async function getData(sLat, sLon, eLat, eLon) {
    let response = await axios.get(api_url, {
        params: {
            srclat: sLat,
            srclon: sLon,
            destlat: eLat,
            destlon: eLon
        }
    })
    .catch(function(error) {
        console.log(error);
        alert(error);
    });
    return response.data;
}
//module.exports = getData;