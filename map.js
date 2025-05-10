
const map = L.map('map').setView([37.7749, -122.4194], 10);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

const airplaneIcon = L.icon({
    iconUrl: 'https://cdn-icons-png.flaticon.com/512/759/759759.png',
    iconSize: [32, 32],
    iconAnchor: [16, 16]
});

L.marker([37.7749, -122.4194], { icon: airplaneIcon })
    .addTo(map)
    .bindPopup('🛫 Sample Flight Location');
