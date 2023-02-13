from django.db.models.signals import post_save,pre_save
from django.dispatch import  receiver
from .models import *





# as per documentation 2 also can be used
@receiver(post_save,sender=User)
def post_save_create_profile_recevier(sender,instance,created,**kwargs):
    
    print(created)
    if created:
        # //if user created then created userprofile
        Userprofile.objects.create(user=instance) 
        print("created user profile thanks you django")

    else:
        try:
          profile=Userprofile.objects.get(user=instance)
          profile.save()
          print('this is upgraded')
        except:
            # create a userprofile if not exist
            Userprofile.objects.create(user=instance) 
            print('profile pic was delted ,i created')



# connecting with user
# 2) post_save.connect(post_save_create_profile_recevier,sender=User)



@receiver(pre_save,sender=User)
def pre_save_create_profile_reciever(sender,instance,**kwargs):
    print(instance.username,'this user is being saved')


