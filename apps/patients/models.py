from django.conf import settings
from django.db import models
from ..doctors.models import Doctor
from ..rooms.models import Room


class Patient(models.Model):

    class Gender(models.TextChoices):
        MALE = "MALE", "Male"
        FEMALE = "FEMALE", "Female"
        OTHER = "OTHER", "Other"

    class BloodGroup(models.TextChoices):
        A_POSITIVE = "A+", "A+"
        A_NEGATIVE = "A-", "A-"
        B_POSITIVE = "B+", "B+"
        B_NEGATIVE = "B-", "B-"
        AB_POSITIVE = "AB+", "AB+"
        AB_NEGATIVE = "AB-", "AB-"
        O_POSITIVE = "O+", "O+"
        O_NEGATIVE = "O-", "O-"

    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="patient")
    doctor =models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name="patient")
    room = models.ForeignKey(Room,on_delete=models.SET_NULL,null=True)
    patient_id = models.CharField( max_length=20,unique=True )
    father_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    gender = models.CharField( max_length=10,choices=Gender.choices)

    blood_group = models.CharField(max_length=3,choices=BloodGroup.choices,blank=True,null=True)

    cnic = models.CharField(max_length=15,unique=True )

    phone_number = models.CharField(max_length=15,unique=True )

    address = models.TextField()

    city = models.CharField( max_length=100)

    emergency_contact_name = models.CharField(max_length=100)

    emergency_contact_phone = models.CharField(max_length=15)

    emergency_contact_relation = models.CharField(max_length=50)

    profile_picture = models.ImageField( upload_to="patients/",blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True )

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient_id} - {self.user.first_name}"