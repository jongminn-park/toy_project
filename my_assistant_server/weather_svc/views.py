from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from . import weather_service


class CurrentWeather(View):
    def get(self, request):
        lat, lng = request.headers['geolocation'].split(',')
        data = weather_service.get_current_weather((lat, lng))
        return JsonResponse(data) 


class Forecast(View):
    def get(self, request):
        lat, lng = request.headers['geolocation'].split(',')
        data = weather_service.get_weather_forecast((lat, lng)) 
        return JsonResponse(data)
