import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import '../components/Home.css'

function Home() {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    const fetchRestaurants = async () => {
      try {
        const response = await fetch('/restaurants');
        const data = await response.json();
        setRestaurants(data);
      } catch (error) {
        console.error('Error fetching restaurants:', error);
      }
    };

    fetchRestaurants();
  }, []);

  return (
    <div>
      {restaurants.map((restaurant) => (
        <div key={restaurant.id} className="restaurant-container">
          <div className="restaurant-info">
            <p>Restaurant: {restaurant.name}</p>
            <p>Address: {restaurant.address}</p>
          </div>
          <Link to={`${window.location.origin}/restaurants/${restaurant.id}`} className="restaurant-link">
            View Details
          </Link>
        </div>
      ))}
    </div>
  );
}

export default Home;