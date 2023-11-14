from flask import Flask, jsonify, request, render_template

# Importing local modules that forecasts weather and provides latitude and longitude
import lat_long
import forecast

app = Flask(__name__)

# Flask decorator for homepage and html links
@app.route('/')
def index():
  return render_template('index.html')

# Function to get input from form and return forecast in json
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
    app.run(host="0.0.0.0") # Running the Flask application on the local network
