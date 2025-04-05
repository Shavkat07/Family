from django.db.models.signals import post_save
from django.dispatch import receiver

from custom_auth.models import User
from profile.models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'profile'):
        Profile.objects.create(user=instance)