from flask import jsonify
import requests

def get_weather(lat, long):
  url = "https://api.open-meteo.com/v1/forecast"
  params = {
    "latitude": lat,
    "longitude": long,
    "current": ["temperature_2m", "rain"],
    "hourly": ["temperature_2m", "rain"],
  }

  response = requests.get(url, params=params)

  return response.json()

