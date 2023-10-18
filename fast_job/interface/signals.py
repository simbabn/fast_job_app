from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile  # Assurez-vous d'importer le modèle UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


    
# @receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
# def save_user_profile(sender, instance, created, **kwargs):
#     user = instance
#     if created:
#         profile = UserProfile(user=user)
#         profile.save()
        #profile.save()