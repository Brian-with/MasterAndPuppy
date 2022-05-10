from django.urls import path
from .views import UserinfoView

urlpatters = [
    path("", UserinfoView.as_view())
]