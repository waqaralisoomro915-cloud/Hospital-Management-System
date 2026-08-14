from django.urls import path
from . import views

urlpatterns = [
    path('hospitalization/', views.hospitalization, name='hospitalization'),
]