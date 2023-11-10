#!/usr/bin/env python3

from geopy.geocoders import Nominatim

def get_lat_long(city):
   geolocator = Nominatim(user_agent="myGeocoder")
   location = geolocator.geocode(city)
   return location.latitude, location.longitude