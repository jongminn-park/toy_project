from wifi import Cell
import requests
import json
import sys

with open('client_config.json', 'r') as f:
    config = json.load(f)

APP_HOST = config["google_geolocate"]["APP_HOST"] 
APP_KEY =  config["google_geolocate"]["APP_KEY"]

def scan_for_cells():
    result = []

    print("looking for AP...")
    while True:
        cells = list(Cell.all('wlan0'))
        if len(cells) > 2:
            break
        
    for cell in cells:
        result.append({
            "macAddress" : cell.address,
            "signalStrength" : cell.signal,
            "channel" : cell.channel
            })

    print("had more than 2 APs")
    return result


def get_geolocation(using_wifiInfo=False):
    url = APP_HOST+APP_KEY
    payload = None
    headers = None

    if using_wifiInfo:
        headers = {'content-type' : 'application/json'}
        payload = json.dumps({"wifiAccessPoints" : scan_for_cells()})

    try:
        resp = requests.post(url, data=payload, headers=headers)
        resp.raise_for_status()
        print("got response from google geolocation api")
        return resp.json()
    except Exception:
        print(resp.status_code)
        sys.exit(1)

