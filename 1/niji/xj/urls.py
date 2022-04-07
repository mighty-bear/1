from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers

from xj import views

urlpatterns = [
    path('李贺', views.LiHe)
]