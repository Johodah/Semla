from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('rate/<int:semla_id>/', views.add_rating, name='rate_semla'),
]
