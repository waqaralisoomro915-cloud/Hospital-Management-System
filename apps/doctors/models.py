from django.db import models
from ..accounts.models import User
from ..departments.models import Department

class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    specialization = models.CharField(max_length=100)
    license_number =models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.specialization} - {self.user.first_name}"