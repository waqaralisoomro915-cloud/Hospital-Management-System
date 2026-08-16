from rest_framework import serializers
from .models import Doctor
from ..accounts.permissions import (IsDoctor,IsAdmin, IsPatient)

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
