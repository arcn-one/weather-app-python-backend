from flask import jsonify
import requests

class Forecast:
   def __init__(self, lat, long):
       self.url = "https://api.open-meteo.com/v1/forecast"
       self.params = {
           "latitude": lat,
           "longitude": long,
           "current": ["temperature_2m", "rain"],
           "hourly": ["temperature_2m", "rain"],
       }
       self.response = self.get_weather()

   def get_weather(self):
       return requests.get(self.url, params=self.params)

   def get_json(self):
       return self.response.json()
