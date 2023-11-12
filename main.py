from flask import Flask, jsonify, request, render_template

import lat_long
import forecast

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def weather_data():
  if request.method == 'POST':
    city = request.form.get('city')
    lat, long = lat_long.get_lat_long(city)
    weather_result = forecast.get_weather(lat, long)
    return jsonify(weather_result)
  else:
    return render_template('html-files/index.html')

if __name__ == "__main__":
    app.run(debug=True)
