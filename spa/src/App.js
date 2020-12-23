import React from 'react';
import './App.css';
import Weather from './Weather';
import {BrowserRouter as Router} from "react-router-dom";


function App() {
    return (
        <Router>
            <div className="container">
                <Weather/>
            </div>
        </Router>
    );
}

export default App;
