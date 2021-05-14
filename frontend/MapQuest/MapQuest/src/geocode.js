// change user input into latitude and longitude cordinates through Geocoding API provided by MapQuest
const geocode_url = "http://www.mapquestapi.com/geocoding/v1/address";
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