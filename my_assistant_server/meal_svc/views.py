from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from . import meal_service 


class Recommendation(View):
    def get(self, request):
        data = meal_service.get_all_menus()
        return JsonResponse(data) 

