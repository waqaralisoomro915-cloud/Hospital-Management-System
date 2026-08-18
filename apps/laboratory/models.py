from django.db import models
from ..patients.models import Patient
from ..doctors.models import Doctor



class Laboratory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT,related_name="laboratory_tests")
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT,related_name="laboratory_tests")
    test_name = models.CharField(max_length = 100)
    test_type = models.CharField(max_length = 100)
    test_date = models.DateField()
    test_result = models.TextField(blank=True, null=True)
    normal_range=models.CharField(max_length = 100,blank=True, null=True)
    status =models.CharField(max_length = 20,
                             choices=[("PENDING","PENDING"),
                                      ("IN_PROGRESS","IN_PROGRESS"),
                                      ("APPROVED","APPROVED"),
                                      ("REJECTED","REJECTED")],
                             default = "PENDING")
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
       return f"{self.test_name} - {self.test_type} - {self.test_date}"
