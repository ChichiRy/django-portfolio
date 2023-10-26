

from django.urls import path
from . import views


app_name = "Portfolio"
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('education/', views.education, name="education"),
    path('work_exp/', views.work_exp, name="work_exp"),
    path('honours/', views.honours, name="honours"),
    path('certifications/', views.certifications, name="certifications"),
    path('projects/', views.projects, name="projects")
]
