import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';


function Pizza() {
  const { id } = useParams();
  const [pizza, setPizza] = useState(null);
  const [error, setError] = useState(null);
  const [status, setStatus] = useState('pending');

  useEffect(() => {
    const fetchPizzaById = () => {
      fetch(`http://127.0.0.1:5000/pizzas/${id}`)
        .then(response => {
          if (response.ok) {
            return response.json();
          } else {
            return response.json().then(err => Promise.reject(err.error));
          }
        })
        .then(pizzaData => {
          setPizza(pizzaData);
          setError(null);
          setStatus('resolved');
        })
        .catch(err => {
          console.error('Error fetching pizza by ID:', err);
          setPizza(null);
          setError('An error occurred while fetching the pizza by ID.');
          setStatus('rejected');
        });
    };

    fetchPizzaById();
  }, [id]);

  if (status === 'pending') return <h1>Loading...</h1>;
  if (status === 'rejected') return <h1>Error: {error}</h1>;

  if (!pizza) {
    return <h1>Pizza not found or invalid</h1>;
  }

  return (
    <div className="container">
      <h2 className="heading">Pizza Details</h2>
      <p className="detailText">
        <strong>Name:</strong> {pizza.name}
      </p>
      <p className="detailText">
        <strong>Ingredients:</strong> {pizza.ingredients}
      </p>
    </div>
  );
}

export default Pizza;