from geopy.geocoders import Nominatim
import json
from urllib.request import urlopen

# Defining a function to get the latitude and longitude of a given city
def get_lat_long(city):
   # Creating an instance of the Nominatim class: without this geocode fails
   geolocator = Nominatim(user_agent="myGeocoder")
   # get precise location using maual entry or gps
   location = geolocator.geocode(city)
   return location.latitude, location.longitude

def get_coarse_location():
   # get coarse location using ip address
   data = json.load(urlopen("http://ipinfo.io/json"))
   ip_latitude = data['loc'].split(',')[0]
   ip_longitude = data['loc'].split(',')[1]
   return ip_latitude, ip_longitude