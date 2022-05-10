import json

from django.http import JsonResponse
from django.views import View

from .models import Owner, Dog

class AddOwner(View):

    def post(self, request):
        input = json.loads(request.body)
        owner = Owner.objects.create(
            name = input["name"],
            email = input["email"],
            age	= input["age"])
        
        return JsonResponse({"message" : "Owner data saved succecefully!"}, status = 201)

class AddDog(View):

    def post(self, request):
        input = json.loads(request.body)
        dog = Dog.objects.create(
            name = input["dog_name"],
            age	= input["dog_age"],
            owner_id = input["owner_id"])
            
        return JsonResponse({"message" : "Dog data saved succecefully!"}, status = 201)