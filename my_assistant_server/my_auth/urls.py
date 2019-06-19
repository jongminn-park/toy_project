from django.urls import path
from .views import Auth

app_name = 'my_auth'
urlpatterns = [
        path('', Auth.as_view())
        ]
