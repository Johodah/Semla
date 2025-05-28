from django.shortcuts import render
from .models import Semla

def home(request):
    semlor = Semla.objects.all()
    return render(request, 'semla_django/home.html', {'semlor': semlor})