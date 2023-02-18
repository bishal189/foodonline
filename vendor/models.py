from django.db import models
from accounts.models import User,Userprofile
from accounts.utils import send_notfication
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
       
    def save(self,*args,**kwargs):
        if self.pk is not None:
            # update
            orginal=vendor.objects.get(pk=self.pk)
            if orginal.is_approved!=self.is_approved:
                if self.is_approved == True:
                    mail_subject='Congrulations! your resturant has been approved.'
                    mail_template='accounts/emails/admin_approval_email.html'
                    context={
                        'user':self.user,
                        'is_approved':self.is_approved
                    }
                    # send notfication emial
                    send_notfication(mail_subject,mail_template,context)
                else:
                    mail_subject='we are sorry! you are not eligible for publishing your food menu on our marketplace'
                    mail_template='accounts/emails/admin_approval_email.html'
                    context={
                        'user':self.user,
                        'is_approved':self.is_approved
                    }
                    
                    
                    send_notfication(mail_subject,mail_template,context)

                    # send notfication email 
                    #    

                   
        return super(vendor,self).save(*args,**kwargs)
