from flask import Flask, jsonify, request, render_template, Response
from flask_cors import CORS
from werkzeug.exceptions import HTTPException
import json
import time

# Importing local modules that forecasts weather and provides latitude and longitude
from location import GetLocation
from forecast import Forecast

app = Flask(__name__)
CORS(app)

@app.before_request
def handle_options():
   if request.method == 'OPTIONS':
       return Response(status=200)

# Flask decorator for homepage and html links
@app.route('/')
def index():
  return jsonify({'message':'welcome to the weatherapp api'})

# Function to get input from form and return forecast in json
@app.route('/submit/<city>', methods=["POST", "GET"])
def weather_data_precise(): 
  try:
    city = request.form.get('city')
    lat, long = GetLocation(city_name=city).get_cordinates()
    weather_result = Forecast(lat=lat, long=long).get_json()
    return jsonify(weather_result)
  except Exception as e:
    app.logger.error(f"An error occurred: {e}")
    return jsonify({"error": "An error occurred"}), 500

# testig coarse location
@app.route('/coarse')
def weather_data_coarse(): 
  try:
    ip_address="8.8.8.8"
    lat, long = GetLocation(ip_address=ip_address).get_cordinates()
    weather_result = Forecast(lat=lat, long=long).get_json()
    return jsonify(weather_result)
  except Exception as e:
    app.logger.error(f"An error occurred: {e}")
    return jsonify({"error": "An error occurred"}), 500

# Handling errors
@app.errorhandler(Exception)
def handle_exceoption(error):
  response = error.get_response()
  response.data = json.dumps({
    "code": error.code,
    "name": error.name,
    "description": error.description,
  })
  app.logger.error(str(error))
  return Response("An error occurred", status=500)

if __name__ == "__main__":
    app.run(host="0.0.0.0") # Running the Flask application on the local network
