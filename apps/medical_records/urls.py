from django.urls import path
from . import views
urlpatterns = [
    path('medical_record/', views.medical_record, name='medical_record'),
]