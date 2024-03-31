from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers

from fhl import views

urlpatterns = [
    path('', views.index),
    path('start_game', views.start_game),
    path('check_answer', views.check_answer)
]
