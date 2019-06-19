from django.urls import path
from weather_svc.views import CurrentWeather, Forecast 

app_name = 'weather_svc'
urlpatterns = [
        path('current-weather/', CurrentWeather.as_view()),
        path('forecast/', Forecast.as_view()),
        ]
