from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, **kwargs):
    try:
        if instance.profile:
            instance.profile.save()
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance)
