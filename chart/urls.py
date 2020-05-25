from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.test_page, name='chart'),

]