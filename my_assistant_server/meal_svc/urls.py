from django.urls import path
from meal_svc.views import Recommendation


app_name = 'meal_svc'
urlpatterns = [
        path('recommendation', Recommendation.as_view()),
        ]
