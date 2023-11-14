from geopy.geocoders import Nominatim

# Defining a function to get the latitude and longitude of a given city
def get_lat_long(city):
   # Creating an instance of the Nominatim class: without this geocode fails
   geolocator = Nominatim(user_agent="myGeocoder")
   location = geolocator.geocode(city)
   return location.latitude, location.longitude