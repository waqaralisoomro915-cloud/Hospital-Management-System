from rest_framework import serializers
from .models import PrescriptionMedicine

class PrescriptionMedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionMedicine
        fields = '__all__'
