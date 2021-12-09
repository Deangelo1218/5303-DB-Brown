import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Listing from './listing';
import User from './add';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css'

class App extends Component {
  render() {
    return (
      <div className="App list-group-item justify-content-center align-items-center mx-auto" style={{"width":"400px", "backgroundColor":"white", "marginTop":"15px"}}>
      <h1 className="card text-white bg-primary mb-1" styleName="max-width: 20rem;">Advising</h1>
      <h6 className="card text-white bg-primary mb-3">FASTAPI - React - MongoDB</h6>
      <div className="card-body">
        <h5 className="card text-white bg-dark mb-3">Advising Form</h5>
          <span className="card-text">
            <User/>
          </span>
          <h5 className="card text-white bg-dark mt-3">Advising Form</h5>
          <div>
            <Listing/>
          </div>
          
      </div>
      <h6 className="card text-dark bg-warning py-1 mb-0">Copyright 2021, All rights reserved &copy;</h6>
    </div>
  
      
    
    );
  }
}
 
export default App;


