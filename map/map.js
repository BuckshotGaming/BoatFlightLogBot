const map = L.map("map").setView([37.7749, -122.4194], 10);
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution: "© OpenStreetMap"
}).addTo(map);

const airplaneIcon = L.icon({
  iconUrl: "https://cdn-icons-png.flaticon.com/512/159/159604.png",
  iconSize: [32, 32],
  iconAnchor: [16, 16]
});

L.marker([37.7749, -122.4194], { icon: airplaneIcon }).addTo(map)
  .bindPopup("✈️ Sample Aircraft");
