from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group

from accounts.models.user import User
from app.models.profile import Profile
from app.models.client import Client
from app.models.AppSettings import Appsetting

@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, *args, **kwargs):
    
    if created:

        if Group.objects.all().count() <1:
            GROUPS = ['admin', 'staff', 'client']
            for group in GROUPS:
                Group.objects.get_or_create(name=group)
                
        if instance.is_superuser:
            Profile.objects.create(user=instance)            
            newprofile=Profile.objects.get(user=instance)
            newuser = instance
            group = Group.objects.get(name='admin')
            newuser.groups.add(group)
            Client.objects.create(profile = newprofile)

            if Appsetting.objects.all().count() == 0:
                Appsetting.objects.create(name="landing")