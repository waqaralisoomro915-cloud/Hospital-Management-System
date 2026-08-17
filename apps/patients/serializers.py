import re
from datetime import timezone

from rest_framework import serializers

from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields='__all__'

    def validate_date_of_birth(self, date_of_birth):
        if date_of_birth > timezone.now().date():
            raise serializers.ValidationError("Date of birth must be in the future")
        return date_of_birth

    def validate_cnic(self,cnic):
        pattern = r"^\d{5}-\d{7}-\d$"
        if not re.match(pattern,cnic):
            raise serializers.ValidationError("CNIC must not contain special characters")
        return cnic

    def validate_emergency_contact_phone(self,emergency_contact_phone):
        pattern = r"^\+92\d{10}$"
        if not re.match(pattern,emergency_contact_phone):
            raise serializers.ValidationError("Phone number must be in the format 03001234567.")
        return emergency_contact_phone

    def validate_emergency_contact_relation(self, emergency_contact_relation):
        pattern = r"^[A-Za-z ]+$"

        if not re.match(pattern, emergency_contact_relation):
            raise serializers.ValidationError(
                "Emergency contact relation must contain only letters."
            )

        return emergency_contact_relation