from django.db import models
from django.core.exceptions import ValidationError

from ..patients.models import Patient
from ..doctors.models import Doctor
from ..departments.models import Department
from ..rooms.models import Room


class Hospitalization(models.Model):

    class AdmissionType(models.TextChoices):
        EMERGENCY = "EMERGENCY", "Emergency"
        SCHEDULED = "SCHEDULED", "Scheduled"
        REFERRAL = "REFERRAL", "Referral"

    class Status(models.TextChoices):
        ADMITTED = "ADMITTED", "Admitted"
        DISCHARGED = "DISCHARGED", "Discharged"
        CANCELLED = "CANCELLED", "Cancelled"
    #relation with pateient
    patient = models.ForeignKey( Patient,on_delete=models.PROTECT, related_name="hospitalizations")
    # relation with  doctor
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT,related_name="hospitalizations" )
    # relation with department
    department = models.ForeignKey( Department,on_delete=models.PROTECT,related_name="hospitalizations")
    # relation with room
    room = models.ForeignKey(Room,on_delete=models.PROTECT,related_name="hospitalizations")

    admission_date = models.DateTimeField()
    discharge_date = models.DateTimeField( null=True, blank=True )
    admission_type = models.CharField(max_length=20,choices=AdmissionType.choices, default=AdmissionType.SCHEDULED )
    reason = models.TextField()
    diagnosis = models.TextField(blank=True,null=True)
    status = models.CharField( max_length=20, choices=Status.choices,default=Status.ADMITTED )
    notes = models.TextField(blank=True,null=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.patient} - {self.admission_date}"