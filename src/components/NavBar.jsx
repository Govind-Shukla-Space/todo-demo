import './NavBar.css';
import React from 'react'

function NavBar() {
  const name="PSIT";
  const clickHandler=()=>{
    console.log("button pressed");
  }
  return (<>
    <p>This is "{name}"</p>
    <p>this is in console {console.log("Hello")}</p>
    <button onClick={clickHandler}>Click me</button>
    </>
  )
}

export  default NavBar;