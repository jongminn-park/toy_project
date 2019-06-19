# weather_service.py
import requests
import sys
sys.path.append("..")
from my_lib import helper_funcs

config = helper_funcs.read_config_file()

API_HOST = config['ROUTING_SVC']['API_HOST']
CLIENT_ID_HEADER = config['ROUTING_SVC']['CLIENT_ID_HEADER']
CLIENT_SECRET_HEADER = config['ROUTING_SVC']['CLIENT_SECRET_HEADER']
CLIENT_ID = config['ROUTING_SVC']['CLIENT_ID']
CLIENT_SECRET = config['ROUTING_SVC']['CLIENT_SECRET']

def get_route(start, goal):
    start_geo = ",".join(start)
    goal_geo = ",".join(goal)
    routing_query = "?start="+start_geo+"&goal="+goal_geo+"&option=trafast"

    uri = API_HOST + routing_query 
    headers = {
            CLIENT_ID_HEADER: CLIENT_ID,
            CLIENT_SECRET_HEADER: CLIENT_SECRET
            }

    with requests.get(uri, headers=headers) as resp:
        result = resp.json()

    return result 


