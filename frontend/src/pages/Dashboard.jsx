import React, { useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet'; // You need to import the 'leaflet' library
import redMarkerIcon from '../assets/red_marker-icon.png';

const Dashboard = () => {
  const [position, setPosition] = useState([13.082680, 80.270721]);
  const [newLat, setNewLat] = useState(null);
  const [newLng, setNewLng] = useState(null);
  const [mapKey, setMapKey] = useState(0); // Add a key for MapContainer

  // Create a custom red marker icon
    const customMarkerIcon = new L.Icon({
    iconUrl: redMarkerIcon,
    iconSize: [32, 32], // Set the size of the red marker icon
    iconAnchor: [16, 32], // Set the anchor point to half the height of the icon
  });

  
  const handleLatChange = (e) => {
    const lat = parseFloat(e.target.value);
    setNewLat(!isNaN(lat) ? lat : '');
  };

  const handleLngChange = (e) => {
    const lng = parseFloat(e.target.value);
    setNewLng(!isNaN(lng) ? lng : '');
  };

  const handleUpdateMap = () => {
    if (!isNaN(newLat) && !isNaN(newLng)) {
      setPosition([newLat, newLng]);
      setMapKey((prevKey) => prevKey + 1); // Change the key to trigger a reload
    }
  };

  return (
    <div className='flex flex-row bg-white'>
      <div className='w-1/2'>
          <h1>hello</h1>
      </div>
      <div className='h-[900px] border border-black p-[5px] rounded  w-1/2'>
          <MapContainer
            key={mapKey} // Set the key to trigger a reload
            center={position}
            zoom={13}
            className='h-full w-full'
          >
            <TileLayer
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
              attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            />
            <Marker position={position} icon={customMarkerIcon}>
              <Popup>
                Latitude: {position[0]}, Longitude: {position[1]}
              </Popup>
            </Marker>
          </MapContainer>
        </div>
    </div> 
  );
};

export default Dashboard;
