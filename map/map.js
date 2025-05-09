
var map = L.map('map').setView([37.7749, -122.4194], 5); // Default center

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Example marker (can be replaced with live data)
L.marker([37.7749, -122.4194]).addTo(map)
    .bindPopup('Sample Aircraft<br>Altitude: 12000 ft')
    .openPopup();
