from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='chart'),
    path('ci', views.GJ_index, name='ci'),
    path('ca', views.JN_index, name='ca'),
    path('chart', views.chart_page, name="char"),
    path('search', views.search, name='search'),
    path('main', views.main_page, name="main")

]