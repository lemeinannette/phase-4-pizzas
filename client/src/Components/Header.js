import React from 'react';
import { Link } from 'react-router-dom';
import '../components/Header.css'

function Header() {
  return (
    <header>
      <h1>
        <Link to="/">Pizza Restaurants</Link>
      </h1>
    </header>
  );
}

export default Header;