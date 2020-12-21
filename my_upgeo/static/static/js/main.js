
// Configuring Leaflet JS
const cities = {
    nozha: [30.111944096830296, 31.398968696594242],
    madenati: [30.08974158031625, 31.632041931152347]
}

const map = L.map('map').setView(cities.nozha, 15);


// OpenStreetMap Tile
// L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
//     attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
// }).addTo(map);


// Mapbox Tile
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoibXVoYW1lZHlvdXNzZWYiLCJhIjoiY2s3cnBhdG00MGVtajNucWQyeDZhanVqdiJ9.ejPNZfqzS3AY0ctYG_4zeg'
}).addTo(map);


// Map events
map.on('click', e => console.log(e.latlng))


// Custom marker
const carIcon = L.icon({
    iconUrl: 'img/truck-solid.svg',
    iconSize:     [40, 40],
});

carMarker = L.marker([30.08981584453616, 31.630325317382816], {icon: carIcon, rotationAngle: 50}).addTo(map);
carMarker.bindPopup("Hey, i'm a Car")






// Playing around

// map.locate().on('locationfound', e => map.flyTo([e.latlng.lat, e.latlng.lng]))

document.querySelectorAll('.goTo').forEach(btn => {
    btn.addEventListener('click', e => {
        const city = btn.dataset.city;
        map.flyTo(cities[city])
    })
})





// Create some bins
const BinIcon = L.Icon.extend({
    options: {
        iconSize: [25, 25]
    }
})

const fullBinIcon = new BinIcon({iconUrl: 'img/trash-full.svg'});
const semifullBinIcon = new BinIcon({iconUrl: 'img/trash-semifull.svg'});
const emptyBinIcon = new BinIcon({iconUrl: 'img/trash-empty.svg'});



// Add bins to the map
let bins = [];
garbageBins.forEach((bin, index) => {
    if (bin.length == 0) return bins.push({});

    if (index%2 > 0) {
        binMarker = L.marker(bin, {icon: fullBinIcon}).addTo(map);
        binMarker.percentage = 100;
    } else {
        binMarker = L.marker(bin, {icon: semifullBinIcon}).addTo(map);
        binMarker.percentage = 50;
    }


    // attach event
    binMarker.on('click', e => console.log(e.target));

    // Set the z-index
    binMarker.setZIndexOffset(1000);

    // Bind popup
    binMarker.bindPopup(`<p class="m-0">Bin ID: 4896</p><p class="m-0">Percentage: ${binMarker.percentage}%</p>`);

    // Append to the array
    bins.push(binMarker);
});


// Open popup for first bin
bins[1].openPopup()










// Add car route on map
// const polyline = L.polyline(carRoute).addTo(map);
// console.log(polyline)


// Using the antPath
const options = {
    "delay": 400,
    "dashArray": [
        10,
        20
    ],
    "weight": 5,
    "color": "#ff0004",
    "pulseColor": "#FFFFFF",
    "paused": false,
    "reverse": false,
    "hardwareAccelerated": true
}
    
antPolyline = L.polyline.antPath(carRoute, options);
antPolyline.addTo(map);



// Animate marker plugin
const myMovingMarkerOptions = {
    icon: carIcon,
    // loop: true,
    // rotationAngle: 55,
    rotationOrigin: 'center'
}
var myMovingMarker = L.Marker.movingMarker(carRoute, 8*1000, myMovingMarkerOptions).addTo(map);

myMovingMarker.start();
myMovingMarker.addStation(1, 1000)
myMovingMarker.addStation(5, 1000)
myMovingMarker.addStation(8, 1000)



let station = false;

myMovingMarker.addEventListener('move', e => {
    
    // Update the bin status when marker in station
    if (e.oldLatLng == e.latlng) updateBinStatus();


    // Check if the marker finshed the path
    if (e.latlng == myMovingMarker._latlngs[myMovingMarker._latlngs.length-1]) {
        setTimeout(stepTwo, 100);
    }


    for (let i = 1; i < carRoute.length -1; i++ ) {
        if (e.latlng.lat == carRoute[i][0]) {
            station = true;
            return
        }
        
    }

    station = false;
})



// Setting up some vars and check on them every 600ms
let currentBin
let capacity = 10000;
let max_load = 3000;
let log_index = 0


setInterval(() => {
    if (station) {
        incCounters(max_load);
        incPercentage(max_load, capacity);
        appendLog(log_index)

        let bin  = bins[myMovingMarker._currentIndex + 1];
        bin._popup.setContent(`<p class="m-0">Bin ID: 4896</p><p class="m-0">Percentage: 0%</p>`)

        max_load += 2000;
        log_index ++;
    }
}, 600);



// Update bin status
function updateBinStatus(type='EMPTY') {
    setTimeout(() => {
        let bin  = bins[myMovingMarker._currentIndex + 1];
        // Check for empty obj
        if (Object.keys(bin).length === 0 && bin.constructor === Object || bin == undefined) return;

        switch(type) {
            case 'FULL':
                bin.setIcon(fullBinIcon);
                return
            case 'SEMIFULL':
                bin.setIcon(semifullBinIcon);
                return
            case 'EMPTY':
                bin.setIcon(emptyBinIcon);
                return
        };
    }, 600);
}






// Step two
function stepTwo() {
    // Move to this location
    map.flyTo({lat: 30.118236377740057, lng: 31.407122611999515}, 16);

    // remove old stuff
    myMovingMarker.remove();
    antPolyline.remove();


    // add the collection point
    const collectionIcon = L.icon({iconUrl: 'img/garbage.svg', iconSize: [40, 40]});


    // Add collection bin
    collectionBin = L.marker({lat: 30.123117723686967, lng: 31.402616500854496}, {icon: collectionIcon}).addTo(map);

    const newRoute = [
        [30.122941405505085, 31.399194002151493],
        [30.122783646864974, 31.402611136436466]
    ];

    const newMovingMarker = L.Marker.movingMarker(newRoute, 6*1000, myMovingMarkerOptions).addTo(map);
    newMovingMarker.start();



    newMovingMarker.addEventListener('move', e => {
        // the new marker stoped
        if (e.latlng == newMovingMarker._latlngs[newMovingMarker._latlngs.length - 1]) {
            incCounters(0);
            appendLog(3);
        }
    })



    


}





