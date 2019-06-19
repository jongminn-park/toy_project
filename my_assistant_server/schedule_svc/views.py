from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from . import calendar_service
from . import routing_service
from . import geocoding_service
import sys
sys.path.append('..')
from my_auth.models import MyUser
from datetime import datetime

class Today(View):
    def get(self, request):
        return HttpResponse('hi') 


class NextSchedule(View):
    def get(self, request):
        auth_token = request.headers['myauth']

        lat, lng = request.headers['geolocation'].split(',')
        geo_location, f_address = geocoding_service.get_formatted_geo_location((lat, lng))
        start = (str(geo_location['lng']),str(geo_location['lat']))
        
        next_event = calendar_service.get_next_event(auth_token)
        if next_event == "no event":
            return JsonResponse({"answer":"no event"})

        geo_location = geocoding_service.get_geocoding(next_event['location'])
        goal = (str(geo_location['lng']), str(geo_location['lat'])) 

        result = routing_service.get_route(start, goal)
        result["event_start_time"] = next_event["time"]
        result["event_title"] = next_event["title"]
        result["origin"] = f_address
        result["dest"] = next_event['location']
        return JsonResponse(result) 
