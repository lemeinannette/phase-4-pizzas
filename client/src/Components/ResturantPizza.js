import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";


function RestaurantPizza() {
  const [restaurants, setRestaurants] = useState([]);
  const [pizzas, setPizzas] = useState([]);
  const [restaurantId, setRestaurantId] = useState("");
  const [pizzaId, setPizzaId] = useState("");
  const [quantity, setQuantity] = useState("");
  const [formErrors, setFormErrors] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    // Fetch all available pizzas
    fetch("/pizzas")
      .then((r) => r.json())
      .then(setPizzas);

    // Fetch all available restaurants
    fetch("/restaurants")
      .then((r) => r.json())
      .then(setRestaurants);
  }, []);

  function handleSubmit(e) {
    e.preventDefault();
    const formData = {
      restaurant_id: restaurantId,
      pizza_id: pizzaId,
      quantity,
    };

    fetch("/restaurant_pizzas", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
      .then((r) => {
        if (r.ok) {
         
          navigate(`/restaurants/${restaurantId}`);
          window.location.reload();
        } else {
          r.json().then((err) => setFormErrors(err.errors));
        }
      })
      .catch((error) => console.error("Error submitting form:", error));
  }

  return (
    <div className="form-container">
      <form onSubmit={handleSubmit} className="pizza-form">
        <label htmlFor="pizza_id">Pizza:</label>
        <select
          id="pizza_id"
          name="pizza_id"
          value={pizzaId}
          onChange={(e) => setPizzaId(e.target.value)}
        >
          <option value="">Select a pizza</option>
          {pizzas.map((pizza) => (
            <option key={pizza.id} value={pizza.id}>
              {pizza.name}
            </option>
          ))}
        </select>
        <label htmlFor="restaurant_id">Restaurant:</label>
        <select
          id="restaurant_id"
          name="restaurant_id"
          value={restaurantId}
          onChange={(e) => setRestaurantId(e.target.value)}
        >
          <option value="">Select a restaurant</option>
          {restaurants.map((restaurant) => (
            <option key={restaurant.id} value={restaurant.id}>
              {restaurant.name}
            </option>
          ))}
        </select>
        <label htmlFor="quantity">Quantity:</label>
        <input
          type="text"
          id="quantity"
          name="quantity"
          value={quantity}
          onChange={(e) => setQuantity(e.target.value)}
        />
        {formErrors.length > 0 &&
          formErrors.map((err) => (
            <p key={err} className="error-message">
              {err}
            </p>
          ))}
        <button type="submit" className="submit-button">
          Add
        </button>
      </form>
    </div>
  );
}

export default RestaurantPizza;