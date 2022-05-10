from django.urls import path
from .views import AddOwner, AddDog

urlpatterns = [
    path("Add-Owner", AddOwner.as_view()),
    path("Add-Dog", AddDog.as_view()),
]