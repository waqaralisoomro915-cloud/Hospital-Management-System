import re

from rest_framework import serializers


from .models import Nurse


class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = '__all__'

    def validate_cnic(self,cnic):
        pattern = r"^\d{5}-\d{7}-\d$"
        if not re.match(pattern,cnic):
            raise serializers.ValidationError("CNIC must not contain special characters")
        return cnic
    def validate_nurse_number(self,nurse_number):
        pattern = r"^\+92\d{10}$"
        if not re.match(pattern,nurse_number):
            raise serializers.ValidationError("Phone number must be in the format 03001234567.")
        return nurse_number
