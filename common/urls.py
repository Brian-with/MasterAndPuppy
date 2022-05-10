from django.urls import path
from .views import AddOwner, AddDog

urlpatterns = [
    path("/AddOwner", AddOwner.as_view()),
    path("/AddDog", AddDog.as_view()),
]