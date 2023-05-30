from django.urls import path
from . import views

urlpatterns = [
    path('test', views.test),
    path('locationProcess', views.locationProcess),
    path('yxProcess', views.yxProcess)
]
