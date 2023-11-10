from flask import Flask, jsonify

import lat_long
import forecast

app = Flask(__name__)

@app.route('/')
def weather_data():
  lat, long = lat_long.get_lat_long('Colombo, Lk')
  weather_result = forecast.get_weather(lat, long)
  return jsonify(weather_result)

if __name__ == "__main__":
    app.run(debug=True)
