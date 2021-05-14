// Test file for index.html
// Attempted to use Jest testing framework but could not get 'axios' working with the framework
// Jest attempt found at the bottom

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

// comparative function
const equals = (a, b) =>
  a.length === b.length &&
  a.every((v, i) => v === b[i]);

// fetch data from api
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
    });
    return response.data;
}

// convert starting location address to latitude and longitude cordinates
async function getStart(startLoc) {
    let response = await axios.get(geocode_url, {
        params: {
            key: 'ObOOcgLBayNvuhkFMUAKvmh5y7pXteON',
            location: startLoc
        }
    })
    .catch(function(error) {
        console.log(error);
        alert("Please Enter a Valid Address");
    });
    return response.data;
}

// convert destination address to latitude and longitude cordinates
async function getDest(destLoc) {
    let response = await axios.get(geocode_url, {
        params: {
            key: 'ObOOcgLBayNvuhkFMUAKvmh5y7pXteON',
            location: destLoc
        }
    })
    .catch(function(error) {
        console.log(error);
        alert("Please Enter a Valid Address");
    });
    return response.data;
}

// get the maneuver points of route provided by local API
function routing(apiResponse) {
    var maneuverComponents = apiResponse.path.legs[0].maneuvers;
    var routeComponentsLat = [];
    var routeComponentsLon = [];
    for(var i = 0; i < maneuverComponents.length; i++) {
        routeComponentsLat[i] = maneuverComponents[i].startPoint.lat;
        routeComponentsLon[i] = maneuverComponents[i].startPoint.lng;
        var maneuverCord = [routeComponentsLat[i], routeComponentsLon[i]];

        // compare what is returned from API with what is expected
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
    // ensure that a boolean is returned by the API
    if(typeof apiResponse.is_above_avg === "boolean"){
        console.log("PASS: is_above_average value is a boolean");
    }
    else{
        console.log("FAIL: is_above_average value is not a boolean");
    }
}

// Function that Builds the Table from JSON array
function buildTable(apiResponse) {
    var response = apiResponse.results[0];

    // compare what is returned from API with what is expected
    // ensure all properties of the JSON object are proper variable types
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

async function main() {
    //getLatLon(srcLocation, desLocation);
    let startResp = await getStart(srcLocation);
    let startLat = startResp.results[0].locations[0].latLng.lat;
    let startLon = startResp.results[0].locations[0].latLng.lng;
    let destResp = await getDest(desLocation);
    let destLat = destResp.results[0].locations[0].latLng.lat;
    let destLon = destResp.results[0].locations[0].latLng.lng;
    let apiData = await getData(startLat, startLon, destLat, destLon);
    routing(apiData);
    buildAboveAverage(apiData);
    buildTable(apiData);
}

// time the test response time
function start() {
    startTime = new Date();
    main();
};

function end() {
    endTime = new Date();
    var timeDiff = endTime - startTime;
    console.log(timeDiff + " ms");
}

// starts the test
start();



/*
import axios from 'axios';

const srcLocation = "11611 Euclid Ave";
const desLocation = "5300 Riverside Dr";
const srcLat = 41.510853;
const srcLon = -81.602861;
const desLat = 41.411359;
const desLon = -81.837581;
const srcCord = [srcLat, srcLon];
const desCord = [desLat, desLon];
const manLat = 41.51083;
const manLon = -81.602837;
const manCord = [manLat, manLon];
const above_avg = false;

jest.mock('axios');

const getData = require('./getapidata');
var apiData;

async function fetchData() {
    apiData = await getData(srcLat, srcLon, desLat, desLon);
}
fetchData();

test('data fetched from api should be defined', () => {
    expect(apiData).toBeDefined();
});

test('JSON object returned from api should have is_above_avg, path, and results properties', () => {
    expect(apiData).toHaveProperty('is_above_avg');
    expect(apiData).toHaveProperty('path');
    expect(apiData).toHaveProperty('results');
});
*/