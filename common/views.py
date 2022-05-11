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


class OwnerInfo(View):

    def get(self, request):
        output = []
        owners = Owner.objects.all()

        for owner in owners:
            output.append({
                "id"    :   owner.id,
                "name"  :   owner.name,
                "email" :   owner.email,
                "age"   :   owner.age,
            })
        return JsonResponse({"Owner": output}, status = 200)

class DogInfo(View):
    def get(self, request):
        output = []
        dogs = Dog.objects.all()
        owners = Owner.objects.all()

        for dog in dogs:
            output.append({
                "id"    :   dog.id,
                "name"  :   dog.name,
                "age"   :   dog.age,
                "owner_name"    : owners.get(id=dog.owner_id).name
            })
        return JsonResponse({"Dog": output}, status = 200)

class OwnerDogInfo(View):
    def get(self, request):
        output = []
        owners = Owner.objects.all()
        
        for owner in owners:
            dogs = Dog.objects.filter(owner_id=owner.id)
            dog_list = []

            for dog in dogs:
                dog_list.append({
                    "name" : dog.name,
                    "age" : dog.age,
                })

            output.append({
                "name"  :   owner.name,
                "age"   :   owner.age,
                "email" :   owner.email,
                "dogs"  :   dog_list,
            })
        
        return JsonResponse({"Owners and Dogs": output}, status = 200)

"""
# Case 1. 단순 2종 for문 사용
for owner in owners:
    dog_list =[]

    # first, make `dog list`
    for dog in owner.dog_set.all():
        dog_list.append({
            "id"    : 
            "name"  : 
            "age"   :
        })

# Case 2. List comprehension 사용
for owner in owners:

"""