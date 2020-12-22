import requests
from datetime import datetime


class OpenWeather:
    API_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    ICON_URL = "http://openweathermap.org/img/wn/{}@2x.png"

    def __init__(self, location, api_key=None):
        self.api_key = api_key
        self.location = location
        self.kelvin_temp = None
        self.lat = None
        self.lon = None
        self.kelvin_feels_like = None
        self.meters_sec_wind = None
        self.humidity = None
        self.description = None
        self.icon = None
        self.status_code = None
        self.updated = None

        self.update()

    def update(self):
        response = requests.get(self.API_URL.format(self.location, self.api_key))
        self.status_code = response.status_code
        if self.status_code == 200:
            weather_data = response.json()
            if 'coord' in weather_data:
                self.lat = weather_data.get('coord').get('lat')
                self.lon = weather_data.get('coord').get('lon')
            if 'main' in weather_data:
                self.kelvin_temp = weather_data.get('main').get('temp')
                self.kelvin_feels_like = weather_data.get('main').get('feels_like')
                self.humidity = weather_data.get('main').get('humidity')
            if 'weather' in weather_data:
                self.description = list(map(lambda x: x.get('description'), weather_data.get('weather')))
                self.icon = self.ICON_URL.format(weather_data.get('weather')[0].get("icon"))
            if 'wind' in weather_data:
                self.meters_sec_wind = weather_data.get('wind').get('speed')
        self.updated = datetime.now()
