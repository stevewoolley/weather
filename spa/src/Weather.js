import React from 'react';
import Card from 'react-bootstrap/Card';
import './Weather.css';

const Weather = () => {

    return (
        <>
            <Card>
                <Card.Header>Header</Card.Header>
                <Card.Body>
                    <Card.Title>Title</Card.Title>
                    <Card.Subtitle>SubTitle</Card.Subtitle>
                    <Card.Text>Body</Card.Text>
                </Card.Body>
                <Card.Footer>Footer</Card.Footer>
            </Card>
        </>
    )
}

export default Weather