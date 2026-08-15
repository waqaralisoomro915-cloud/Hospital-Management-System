import re
from datetime import timezone

from rest_framework import serializers

from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields='__all__'

    def validate(self, data):
        date_of_birth = data.get('date_of_birth')
        if date_of_birth > timezone.now().date():
            raise serializers.ValidationError("Date of birth must be in the future")
        return data

    def validate(self,data):
        cnic =data.get('cnic')
        pattern = r"^\d{5}-\d{7}-\d$"
        if not re.match(pattern,cnic):
            raise serializers.ValidationError("CNIC must not contain special characters")
        return data

    def validate(self,data):
        emergency_contact_phone = data.get('emergency_contact_phone')
        pattern = r"^\+92\d{10}$"
        if not re.match(pattern,emergency_contact_phone):
            raise serializers.ValidationError("Phone number must be in the format 03001234567.")
        return data

    def validate(self,data):
        emergency_contact_relation=data.get('emergency_contact_relation')
        pattern = r"^\+92\d{10}$"
        if not re.match(pattern,emergency_contact_relation):
            raise serializers.ValidationError("Emergency contact relation Phone number must be in the format 03001234567.")
        return data