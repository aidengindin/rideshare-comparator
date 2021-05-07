import axios from 'axios';

const api_url = 'http://127.0.0.1:5000/';
const geocode_url = "http://www.mapquestapi.com/geocoding/v1/address";

var srcLocation = "11611 Euclid Ave";
var desLocation = "5300 Riverside Dr";
var srcLat = 41.510853;
var srcLon = -81.602861;
var desLat = 41.411359;
var desLon = -81.837581;
var srcCord = [srcLat, srcLon];
var desCord = [desLat, desLon];
var manLat = 41.51083;
var manLon = -81.602837;
var manCord = [manLat, manLon];
var startTime, endTime;

const equals = (a, b) =>
  a.length === b.length &&
  a.every((v, i) => v === b[i]);

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
        routing(response);
        buildAboveAverage(response);
        buildTable(response);
    })
    .catch(function(error) {
        console.log(error);
    })
}

function getLatLon(startLoc, destLoc) {
    var startLat, startLon, endLat, endLon;
    axios.get(geocode_url, {
        params: {
            key: 'ObOOcgLBayNvuhkFMUAKvmh5y7pXteON',
            location: startLoc
        }
    })
    .then(function(response) {
        // save starting location's latitude and longitude cordinates
        startLat = response.data.results[0].locations[0].latLng.lat;
        startLon = response.data.results[0].locations[0].latLng.lng;
    })
    .catch(function(error) {
        console.log(error);
        console.log("Please Enter a Valid Address");
    });

    axios.get(geocode_url, {
        params: {
            key: 'ObOOcgLBayNvuhkFMUAKvmh5y7pXteON',
            location: destLoc
        }
    })
    .then(function(response) {
        // save destinations latitude and longitude cordinates
        endLat = response.data.results[0].locations[0].latLng.lat;
        endLon = response.data.results[0].locations[0].latLng.lng;
    })
    .then(function(response) {
        getData(startLat, startLon, endLat, endLon);

        var startCord = [startLat, startLon];
        var endCord = [endLat, endLon];
               
        if (equals(startCord, srcCord)) {
            console.log("PASS: starting cordinates are equal to 41.51083,-81.602861");
        }
        else {
            console.log("FAIL: starting cordinates are not equal to 41.51083,-81.602837");
        }

        if (equals(endCord, desCord)) {
            console.log("PASS: destination cordinates are equal to 41.411359,-81.837581");
        }
        else {
            console.log("FAIL: destination cordinates are not equal to 41.411359,-81.837581");
        }
    })
    .catch(function(error) {
        console.log(error);
        console.log("Please Enter A Valid Address");
    });
}

// get the maneuver points of route provided by local API
function routing(apiResponse) {
    var maneuverComponents = apiResponse.data.path.legs[0].maneuvers;
    var routeComponentsLat = [];
    var routeComponentsLon = [];
    for(var i = 0; i < maneuverComponents.length; i++) {
        routeComponentsLat[i] = maneuverComponents[i].startPoint.lat;
        routeComponentsLon[i] = maneuverComponents[i].startPoint.lng;
        var maneuverCord = [routeComponentsLat[i], routeComponentsLon[i]];

        if (i === 0) {
            if (equals(maneuverCord, manCord)) {
                console.log("PASS: cordinates for the first maneuver is equal to 41.51083, -81.602837");
            }
            else {
                console.log("FAIL: cordinates for the first maneuver is not equal to 41.51083, -81.602837")
            }
        }
    }
}

// Function that Builds the Div from above average array
function buildAboveAverage(apiResponse) {
    if(typeof apiResponse.data.is_above_avg === "boolean"){
        console.log("PASS: is_above_average value is a boolean");
    }
    else{
        console.log("FAIL: is_above_average value is not a boolean");
    }
}

// Function that Builds the Table from JSON array
function buildTable(apiResponse) {
    var response = apiResponse.data.results[0];
    if(typeof response.provider === "string" && response.provider === "Uber"){
        console.log("PASS: the provider of the first entree is the string Uber");
    }
    else{
        console.log("FAIL: the provider of the first entree is not the string Uber");
    }
    if(typeof response.name === "string" && response.name === "UberX"){
        console.log("PASS: the name of the first entree is the string UberX");
    }
    else{
        console.log("FAIL: the name of the first entree is not the string UberX");
    }
    if(typeof response.pickup === "string"){
        console.log("PASS: pickup is a string");
    }
    else{
        console.log("FAIL: pickup is not a string");
    }
    if(typeof response.arrival === "string"){
        console.log("PASS: arrival is a string");
    }
    else{
        console.log("FAIL: arrival is not a string");
    }
    if(typeof response.price === "number"){
        console.log("PASS: price is a number");
    }
    else{
        console.log("FAIL: price is not a number");
    }
    if(typeof response.seats === "number"){
        console.log("PASS: seats is a number");
    }
    else{
        console.log("FAIL: seats is not a number");
    }
    if(typeof response.shared === "boolean"){
        console.log("PASS: shared is a boolean");
    }
    else{
        console.log("FAIL: shared is not a boolean");
    }
    end();
}

function start() {
    startTime = new Date();
};

function end() {
    endTime = new Date();
    var timeDiff = endTime - startTime;
    console.log(timeDiff + " ms");
}

start();
getLatLon(srcLocation, desLocation);