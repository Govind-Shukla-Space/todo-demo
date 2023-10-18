import React from "react";

function DataTypes(){
    const strVar="I am string";
    const numVar=10;
    const boolVar=true;
    const linkVar="https://www.psit.ac.in/";
    const listVar=["what ","is ","your ","name"];
    
    return (
        <div className="Datatypes">
            <h1>{strVar} and {strVar},{boolVar},{numVar}</h1>
            {boolVar? <div> it is true</div>:<p>it is false</p>}
            <h1>
                {listVar}
                </h1>
            <a href={linkVar}>goto psit</a>
            

        </div>
    )
}
export default DataTypes;