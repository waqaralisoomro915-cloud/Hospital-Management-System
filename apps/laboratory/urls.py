from django.urls import path
from . import views

urlpatterns = [
    path('laboratory/', views.laboratory, name='laboratory'),
]