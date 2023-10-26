

from django.urls import path
from . import views


app_name = "Portfolio"
urlpattern = [
    path('', views.home, name="home")
]
    