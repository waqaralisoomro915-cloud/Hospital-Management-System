from django.urls import path
from .views import PatientViewSet
from rest_framework.routers import DefaultRouter

default_router = DefaultRouter()
default_router.register("patients", PatientViewSet, basename="patient")

urlpatterns = default_router.urls