from django.db import models
from ..accounts.models import User
from ..departments.models import Department


class Nurse(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='nurse')
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,blank=True,related_name='nurses')

    nurse_id = models.AutoField(primary_key=True)
    cnic =models.CharField(max_length=15,unique=True)
    nurse_number = models.CharField(max_length=15,unique=True)
    qualification = models.TextField()
    profile_pic = models.ImageField(upload_to='nurse_profile_pic',blank=True)
    nurse_bed_no = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.get_full_name()


