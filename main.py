from flask import Flask, jsonify, request, render_template
from werkzeug.exceptions import HTTPException
import json
import time

# Importing local modules that forecasts weather and provides latitude and longitude
import location
import forecast

app = Flask(__name__)

# Flask decorator for homepage and html links
@app.route('/')
def index():
  return jsonify({'message':'welcome to the weatherapp api'})

# Function to get input from form and return forecast in json
@app.route('/submit/<city>')
def weather_data_precise(): 
  try:
    city = request.form.get('city')
    lat, long = location.GetLocation(city_name=city).get_cordinates()
    weather_result = forecast.get_weather(lat, long)
    return jsonify(weather_result)
  except:
    raise ValueError("An error occured")

# testig coarse location
@app.route('/coarse')
def weather_data_coarse(): 
  try:
    ip_address="8.8.8.8"
    lat, long = location.GetLocation(ip_address=ip_address).get_cordinates()
    weather_result = forecast.get_weather(lat, long)
    return jsonify(weather_result)
  except:
    raise ValueError("An error occured")

# Handling errors
@app.errorhandler(Exception)
def handle_exceoption(error):
  response = error.get_response()
  response.data = json.dumps({
    "code": error.code,
    "name": error.name,
    "description": error.description,
  })
  response.content_type = "application/json"
  return response

if __name__ == "__main__":
    app.run(host="0.0.0.0") # Running the Flask application on the local network
