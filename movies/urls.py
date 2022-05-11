from django.urls import path
from django.http import HttpResponse
from movies.views import ActorInfoView, MovieInfoView
from movies import views

urlpatterns = [
    path("", views.index),
    path("actorinfo", ActorInfoView.as_view()),
    path("movieinfo", MovieInfoView.as_view()),
]