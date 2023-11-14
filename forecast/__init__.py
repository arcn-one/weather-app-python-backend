from flask import jsonify
import requests

# Function to get weather data based on latitude and longitude
def get_weather(lat, long):
  url = "https://api.open-meteo.com/v1/forecast"
  
  # Parameters for the API request
  params = {
    "latitude": lat,
    "longitude": long,
    "current": ["temperature_2m", "rain"],
    "hourly": ["temperature_2m", "rain"],
  }

  # Making a GET request to the API with the specified parameters
  response = requests.get(url, params=params)

  return response.json()

