# weather_service.py
import requests
import sys
sys.path.append("..")
from my_lib import helper_funcs

config = helper_funcs.read_config_file()

API_HOST = config['GEOCODING_SVC']['API_HOST']
API_KEY = config['GEOCODING_SVC']['APP_KEY']

def get_geocoding(address):
    geocoding_query = "?address="+address+"&key="+API_KEY
    uri = API_HOST + geocoding_query

    with requests.get(uri) as resp:
        data = resp.json()

    result = data["results"][0]["geometry"]["location"]
    return result


def get_formatted_geo_location(geo_location):
    geo_location = ",".join(geo_location)
    geocoding_query = "?latlng="+geo_location+"&key="+API_KEY
    uri = API_HOST + geocoding_query

    with requests.get(uri) as resp:
        data = resp.json()

    result = data["results"][0]["geometry"]["location"], data["results"][0]["formatted_address"]
    return result

