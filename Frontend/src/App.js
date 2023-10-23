import React from 'react';
import './App.css';
import NavBar from './components/NavBar' ;
import Datatypes from './components/Datatypes';
function App() {
  const name = "Kavya"
  return (
    <div className="App">
      <NavBar/>
      <Datatypes/>
      <p> This is what App.jsx will returns! name {name}</p>
    </div>
  );
}

export default App;
