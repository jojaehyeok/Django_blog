from django.shortcuts import render
from .models import models
from . import views

# Create your views here.
def test_page(request):
    return render(request, 'chart/home.html')
