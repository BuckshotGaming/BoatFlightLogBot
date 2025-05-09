
var map = L.map('map').setView([37.7749, -122.4194], 5); // Centered over San Francisco by default

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Example aircraft marker (replace with real data later)
L.marker([37.7749, -122.4194]).addTo(map)
    .bindPopup('Sample Aircraft<br>Altitude: 12000 ft')
    .openPopup();
