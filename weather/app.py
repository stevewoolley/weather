import json
from openweather import OpenWeather
from datetimeencoder import DateTimeEncoder
import os


def lambda_handler(event, context):
    params = event
    api_key = os.environ['API_KEY']
    if 'queryStringParameters' in event:
        params = event.get('queryStringParameters')
    weather = OpenWeather(params.get('location'), api_key)
    status_code = weather.status_code
    weather.__dict__.pop('api_key', None)  # hide api_key
    weather.__dict__.pop('status_code', None)  # move status code
    return {
        "statusCode": status_code,
        "body": json.dumps(weather.__dict__, cls=DateTimeEncoder)
    }
