from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name='detail'),
    path('', views.home, name='blog'),
    path('new/', views.new, name='new'),
    path('newblog/',views.blogpost,name='nowblog'),
    path('create/', views.create, name='create'),
]