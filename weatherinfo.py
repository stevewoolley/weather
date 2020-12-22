#!/usr/bin/env python

import argparse
from weather.openweather import OpenWeather
import json
from datetime import datetime
import math

KELVIN = 0
CELSIUS = 1
FAHRENHEIT = 2
MPH = 1
MSEC = 0
_TEMP_SCALES = (KELVIN, CELSIUS, FAHRENHEIT)
_SPEED_SCALES = (MSEC, MPH)
_TEMP_SCALES_LABELS = ['K', 'C', 'F']
_SPEED_SCALES_LABELS = ['meters/sec', 'mph']


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return super().default(o)


def temp_convert(k=None, c=None, f=None):
    if k:
        return k, math.floor(k - 273.15), math.floor((k - 273.15) * (9 / 5) + 32)
    elif c:
        return math.floor(c + 273.15), c, math.floor(c * (9 / 5) + 32)
    elif f:
        return math.floor(((f - 32) * (5 / 9)) + 273.15), math.floor((f - 32) * (5 / 9)), f
    return None


def speed_convert(ms=None, mph=None):
    if ms:
        return ms, math.floor(ms * 2.2369936)
    elif mph:
        return math.floor(mph / 2.2369936), mph
    return None


def temp_scale_label(scale=FAHRENHEIT):
    if scale in _TEMP_SCALES:
        return _TEMP_SCALES_LABELS[scale]
    return None


def speed_scale_label(scale=MPH):
    if scale in _SPEED_SCALES:
        return _SPEED_SCALES_LABELS[scale]


def temperature(kelvin_value, scale=FAHRENHEIT):
    if scale in _TEMP_SCALES:
        return temp_convert(k=kelvin_value)[scale]
    return None


def speed(ms_value, scale=MPH):
    if scale in _SPEED_SCALES:
        return speed_convert(ms=ms_value)[scale]
    return None


if __name__ == "__main__":
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--key", type=str, required=True)
    parser.add_argument("-l", "--location", type=str, required=True)
    args = parser.parse_args()

    weather = OpenWeather(args.location, api_key=args.key)
    if weather.status_code == 200:
        print("location: {} as of {}".format(args.location, weather.updated))
        print("temp: {} {}".format(temperature(weather.kelvin_temp, FAHRENHEIT), temp_scale_label(FAHRENHEIT)))
        print("feels like: {} {}".format(temperature(weather.kelvin_feels_like, FAHRENHEIT), temp_scale_label(FAHRENHEIT)))
        print("humidity: {}".format(weather.humidity))
        print("wind_speed: {} {}".format(speed(weather.meters_sec_wind), speed_scale_label()))
        print("description: {}".format(weather.description))
        weather_dict = weather.__dict__.pop('api_key', None)  # hide api_key
        print("json: {}".format(json.dumps(weather.__dict__, cls=DateTimeEncoder)))
    else:
        print('Error: {}'.format(weather.status_code))
