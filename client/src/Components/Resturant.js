

import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';


function Restaurant() {
  const { id } = useParams();
  const [restaurant, setRestaurant] = useState(null);
  const [error, setError] = useState(null);
  const [status, setStatus] = useState('pending');

  useEffect(() => {
    const fetchRestaurantById = () => {
      fetch(`/restaurants/${id}`)
        .then(response => {
          if (response.ok) {
            return response.json();
          } else {
            return response.json().then(err => Promise.reject(err.error));
          }
        })
        .then(restaurantData => {
          setRestaurant(restaurantData);
          setError(null);
          setStatus('resolved');
        })
        .catch(err => {
          console.error('Error fetching restaurant:', err);
          setRestaurant(null);
          setError('An error occurred while fetching the restaurant.');
          setStatus('rejected');
        });
    };

    fetchRestaurantById();
  }, [id]);

  if (status === 'pending') return <h1>Loading...</h1>;
  if (status === 'rejected') return <h1>Error: {error}</h1>;

  if (!restaurant || !restaurant.pizzas) {
    return <h1>Restaurant data is missing or invalid</h1>;
  }

  return (
    <div className="restaurant-container">
      <h2 className="restaurant-name">{restaurant.name}</h2>
      <p className="restaurant-address">Address: {restaurant.address}</p>
      <h3 className="pizza-list">Pizzas:</h3>
      <ul className="pizza-list">
        {restaurant.pizzas.map((pizza) => (
          <li key={pizza.id} className="pizza-item">
            <Link to={`/pizza/${pizza.id}`}>
              <strong>{pizza.name}</strong> - {pizza.ingredients}
            </Link>
          </li>
        ))}
      </ul>

      <Link to="/restaurant_pizzas" className="add-pizza-button">
        Add 
      </Link>
    </div>
  );
}

export default Restaurant;