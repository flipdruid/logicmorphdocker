import email
import imp
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.tasks import contact_us_mail
from time import sleep
from django.conf import settings
from django.core.mail import send_mail

from accounts.models import User, Profile, Customer
import json


@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)        

@receiver(post_save, sender=Customer)
def post_save_create_profile(sender, instance, created, *args, **kwargs):
    if created:
        lastEntry               =   Customer.objects.last()
        namesubject             =   str(lastEntry.entity_name) + " |" + str(lastEntry.first_name) + " " + str(lastEntry.last_name) + "| Client ID:" + str(lastEntry.id) + "| Sender: " + str(lastEntry.email)
        details                 =   str(lastEntry.details) + "\n\n Created at: " + str(lastEntry.created_at) + "\n Updated at:" + str(lastEntry.updated_at)
        email                   =   str(lastEntry.email)
        
        contact_us_mail.delay(namesubject,  details, email) #(

        # send_mail (
        # subject=namesubject,
        # message=details,
        # from_email=email,
        # recipient_list=[settings.EMAIL_HOST_USER],
        # fail_silently=False
        # )

        # )