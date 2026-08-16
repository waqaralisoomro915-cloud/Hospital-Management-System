from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    specialization = models.CharField(max_length=100,unique=True)
    license_number =models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.specialization} - {self.user.first_name}"