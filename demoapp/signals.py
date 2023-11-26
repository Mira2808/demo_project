
# code
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
 
 
@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        print('inside created')
  
# @receiver(post_save, sender=User) 
# def save_profile(sender, instance, **kwargs):
#     print('inside save_profile')