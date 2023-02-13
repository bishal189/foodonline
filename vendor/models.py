from django.db import models
from accounts.models import User,Userprofile

# Create your models here.

class vendor(models.Model):
    user=models.OneToOneField(User,related_name='user',on_delete=models.CASCADE)
    user_profile=models.OneToOneField(Userprofile,related_name='userprofile',on_delete=models.CASCADE)
    vendor_name=models.CharField(max_length=50)
    vendor_licences=models.ImageField(upload_to='vendor/licences')
    is_approved=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now_add=True)



    def __str__(self) :
        return self.vendor_name;
       
