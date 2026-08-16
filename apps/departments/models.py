from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=200,unique=True)
    description=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=20)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


