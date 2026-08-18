from rest_framework import serializers
from .models import Hospitalization


class HospitalizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hospitalization
        fields = "__all__"

    def validate(self, attrs):

        admission_date = attrs.get(
            "admission_date",
            getattr(self.instance, "admission_date", None)
        )

        discharge_date = attrs.get(
            "discharge_date",
            getattr(self.instance, "discharge_date", None)
        )

        room = attrs.get(
            "room",
            getattr(self.instance, "room", None)
        )

        department = attrs.get(
            "department",
            getattr(self.instance, "department", None)
        )

        # Discharge date validation
        if discharge_date and admission_date:
            if discharge_date < admission_date:
                raise serializers.ValidationError({
                    "discharge_date":
                    "Discharge date cannot be before admission date."
                })

        # Room belongs to selected department
        if room and department:
            if room.department_id != department.id:
                raise serializers.ValidationError({
                    "room":
                    "The selected room does not belong to the selected department."
                })

        return attrs