from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic import View
from my_auth.models import MyUser


class Auth(View):
    def get(self, request):
        auth_token = request.headers['myauth']
        user_ids = [user.user_id for user in MyUser.objects.all()]
        if auth_token in user_ids:
            return HttpResponse()
        else:
            return HttpResponseForbidden()

