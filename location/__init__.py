from geopy.geocoders import Nominatim
import json
from urllib.request import urlopen

# Defining a function to get the latitude and longitude of a given city
def get_precise_location(city):
   # Creating an instance of the Nominatim class: without this geocode fails
   location = Nominatim(user_agent="testapp").geocode(city)
   return location.latitude, location.longitude

def get_coarse_location():
   # get coarse location using ip address
   data = json.load(urlopen("http://ipinfo.io/json"))
   ip_latitude = data['loc'].split(',')[0]
   ip_longitude = data['loc'].split(',')[1]
   return ip_latitude, ip_longitude

