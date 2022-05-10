from django.urls import path
from .views import AddOwner, AddDog, DogInfo, OwnerDogInfo, OwnerInfo

urlpatterns = [
    path("AddOwner", AddOwner.as_view()),
    path("AddDog", AddDog.as_view()),
    path("OwnerInfo", OwnerInfo.as_view()),
    path("DogInfo", DogInfo.as_view()),
    path("OwnerDogInfo", OwnerDogInfo.as_view()),
]