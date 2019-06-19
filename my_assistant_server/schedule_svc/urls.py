from django.urls import path
from .views import Today, NextSchedule

app_name = 'schedule_svc'
urlpatterns = [
        path('today/', Today.as_view()),
        path('next-schedule/', NextSchedule.as_view()),
        ]
