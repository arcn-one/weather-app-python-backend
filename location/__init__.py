from geopy.geocoders import Nominatim
import json
from urllib.request import urlopen
import requests
import gpsd

class GetLocation:
    def __init__(self, city_name=None, ip_address=None, gps_data=None):
        self.geolocator = Nominatim(user_agent = "testUser")
        if city_name is not None:
            self.location = self.geolocator.geocode(city_name) 
        elif ip_address is not None:
            self.location = self.get_coarse_location(ip_address) 
        elif gps_data is not None:
            self.location = self.gps_data()
        else:
            raise ValueError("At least one of the vars must be proviced")

    def get_coarse_location(self, ip_address):
        data = json.load(urlopen(f"http://ipinfo.io/{ip_address}/json"))
        ip_latitude = data['loc'].split(',')[0]
        ip_longitude = data['loc'].split(',')[1]
        return self.geolocator.geocode(f"{ip_latitude},{ip_longitude}")

    def gps_data(self):
        gpsd.connect()
        packet = gpsd.get_current()
        return self.geolocator.geocode(f"{packet.position()[0]},{packet.position()[1]}")

    # get input, city name, ip address or gps data
    def get_cordinates(self):
        if self.location is not None:
            return (self.location.latitude, self.location.longitude)
        else:
            raise ValueError("Location cordinates returned an empty value")
    # translate the input data into latitude and longitude
    # return the longitude and latitude
