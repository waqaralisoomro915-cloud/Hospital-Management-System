from django.db import models
from ..patients.models import Patient
from ..doctors.models import Doctor


class Prescription(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.PROTECT,related_name="prescriptions")

    doctor = models.ForeignKey(
        Doctor,on_delete=models.PROTECT,related_name="prescriptions")

    prescription_date = models.DateField()

    medicines = models.TextField(blank=True,null=True )

    diagnosis = models.TextField(blank=True, null=True )

    instructions = models.TextField( blank=True, null=True)

    notes = models.TextField( blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient} - {self.prescription_date}"

