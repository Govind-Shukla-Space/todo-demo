import React from 'react';
import './App.css';
import NavBar from './components/NavBar';
// import NavBar from './components/NavBar';
import DataTypes from './components/Datatypes';
function App() {
  const name="Kavya"
  return (
    <div className='App'>
    <NavBar/>
    <DataTypes/>
    <p>This is App.js{name}</p> 
    {DataTypes}   
    </div>
    
  );
}

export default App;
