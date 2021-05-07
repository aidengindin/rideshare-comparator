// get the maneuver points of route provided by local API
var plot = document.createElement('plot');
plot.scr='index.html';
document.head.appendChild(plot);

function routing(apiResponse) {
    var maneuverComponents = apiResponse.data.path.legs[0].maneuvers;
    var routeComponentsLat = [];
    var routeComponentsLon = [];
    for(var i = 0; i < maneuverComponents.length; i++) {
        routeComponentsLat[i] = maneuverComponents[i].startPoint.lat;
        routeComponentsLon[i] = maneuverComponents[i].startPoint.lng;
        var maneuverCord = [routeComponentsLat[i], routeComponentsLon[i]];
        console.log("maneuver " + i + " at " + maneuverCord);
    }
    plotRoute(routeComponentsLat, routeComponentsLon);
}

// plot maneuver points on map to display route
function plotRoute(rLats, rLons) {
    var maneuverList = [];

    for(var i = 1; i < rLats.length - 1; i++) {
        maneuverList[i] = L.latLng([rLats[i], rLons[i]]);
    }

    routeDeveloper.route({
        start: L.latLng([rLats[0], rLons[0]]),
        end: L.latLng([rLats[rLats.length - 1], rLons[rLons.length - 1]]),
        waypoints: maneuverList
    });
}