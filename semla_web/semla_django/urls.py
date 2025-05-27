from django.urls import path
from semla_django import views

urlpatterns = [
    path("", views.home, name="home"),
]
