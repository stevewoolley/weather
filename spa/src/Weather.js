import React, {useEffect, useState} from 'react';
import Card from 'react-bootstrap/Card';
import './Weather.css';
import {useLocation} from "react-router-dom";

function useQuery() {
    return new URLSearchParams(useLocation().search);
}

function temp_convert(k_temp, scale) {
    if (scale === 'C') {
        return Math.floor(k_temp - 273.15);
    }
    if (scale === 'K') {
        return Math.floor(k_temp);
    }
    return Math.floor((k_temp - 273.15) * (9 / 5) + 32);
}

function temp_scale(scale) {
    if (scale === 'C') {
        return 'C';
    }
    if (scale === 'K') {
        return 'K';
    }
    return 'F';
}

function wind_convert(msec, scale) {
    if (scale === 'ms') {
        return Math.floor(msec);
    }
    return Math.floor(msec * 2.2369936);
}

function wind_scale(scale) {
    if (scale === 'ms') {
        return 'msec';
    }
    return 'mph';
}

function splitter(a) {
    if (a !== undefined) {
        return a.map((l, i) => (
            <React.Fragment key={i}>{l}{i < (a.length - 1) ? ', ' : ''}</React.Fragment>
        ));
    }
}

const Weather = () => {
    let query = useQuery();
    const weatherurl = "https://iki2s72bdf.execute-api.us-east-1.amazonaws.com/Prod/weather?location=" + query.get('location');
    const [weatherData, setWeatherData] = useState([]);
    useEffect(() => {
        const loadData = async () => {
            const response = await fetch(weatherurl);
            const jsonData = await response.json();
            setWeatherData(jsonData);
        };
        loadData();
    }, [weatherurl]);


    return (
        <>
            <Card>
                <Card.Header>{weatherData.location}</Card.Header>
                <Card.Body>
                    <Card.Title>
                        <h1>{temp_convert(weatherData.kelvin_temp, query.get('scale'))} {temp_scale(query.get('scale'))}</h1>
                    </Card.Title>
                    <Card.Text>
                        <table width="100%">
                            <tr>
                                <td>Feels Like</td>
                                <td align="right">{temp_convert(weatherData.kelvin_feels_like, query.get('scale'))} {temp_scale(query.get('scale'))}</td>
                            </tr>
                            <tr>
                                <td>Humidity</td>
                                <td align="right">{weatherData.humidity} %</td>
                            </tr>
                            <tr>
                                <td>Wind</td>
                                <td align="right">{wind_convert(weatherData.meters_sec_wind, query.get('wind_scale'))} {wind_scale(query.get('wind_scale'))}</td>
                            </tr>
                        </table>
                    </Card.Text>
                </Card.Body>
                <Card.Footer>{splitter(weatherData.description)}</Card.Footer>
            </Card>
        </>
    )
}

export default Weather