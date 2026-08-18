from django.db import models
from ..prescriptions.models import Prescription
class PrescriptionMedicine(models.Model):
    prescription = models.ForeignKey(
        Prescription, on_delete=models.CASCADE,related_name="medicine_details" )

    medicine_name = models.CharField(max_length=150)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    instructions = models.CharField( max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.medicine_name} - {self.dosage}"