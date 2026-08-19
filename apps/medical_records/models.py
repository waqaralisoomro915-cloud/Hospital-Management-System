from django.db import models
from ..patients.models import Patient
from ..doctors.models import Doctor
from ..hospitalization.models import Hospitalization

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.PROTECT,related_name="medical_records" )

    doctor = models.ForeignKey(Doctor,on_delete=models.PROTECT,related_name="medical_records")

    hospitalization = models.ForeignKey(Hospitalization,on_delete=models.PROTECT, related_name="medical_records", blank=True,null=True)

    record_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient} - {self.record_date}"