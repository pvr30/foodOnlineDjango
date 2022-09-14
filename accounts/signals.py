from django.db.models.signals import post_save
from .models import User, UserProfile
from django.dispatch import receiver

@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else: 
        # user profile created if object does not exists
        try:
            user_profile = UserProfile.objects.get(user=instance)
            user_profile.save()
        except: 
            UserProfile.objects.create(user=instance)
            



