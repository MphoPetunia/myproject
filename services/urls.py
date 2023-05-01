from django.contrib import admin
from django.urls import path, include, re_path
from deliveryApp import views
from django.urls import re_path as url

app_name = 'services'
urlpatters = [
    path('',views.service),
]