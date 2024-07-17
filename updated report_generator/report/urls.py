from django.contrib import admin
from django.urls import path, include
from report import views




urlpatterns = [
    path('', views.home, name='home'),
    


]


