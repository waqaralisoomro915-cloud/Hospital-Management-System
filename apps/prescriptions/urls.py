from django.urls import path
from . import views

urlpatterns = [
    path('prescriptions/',views.prescriptions,name='prescriptions'),
]