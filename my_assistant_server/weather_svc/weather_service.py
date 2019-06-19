# weather_service.py
import requests
import os, sys
sys.path.append("..") 
from my_lib import helper_funcs


config = helper_funcs.read_config_file()

API_HOST = config['WEATHER_SVC']['API_HOST']
APP_KEY = config['WEATHER_SVC']['APP_KEY']
FORECAST_5DAY_3HOUR = config['WEATHER_SVC']['FORECAST_5DAY_3HOUR']
CURRENT_WEATHER = config['WEATHER_SVC']['CURRENT_WEATHER']

def req(method, geo_location):
    latitude, longitude = geo_location
    geo_query = "?lat="+latitude+"&lon="+longitude
    uri = API_HOST + method + geo_query + "&appid="+APP_KEY
    response = requests.get(uri)
    
    return response.json()


def get_weather_forecast(geo_location):
    weather_data = req(FORECAST_5DAY_3HOUR, geo_location)
    return weather_data


def get_current_weather(geo_location):
    weather_data = req(CURRENT_WEATHER, geo_location)
    return weather_data

