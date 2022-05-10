from django.urls import path
from .views import UserinfoView

urlpatterns = [
    path("", UserinfoView.as_view()),
]