from __future__ import absolute_import

from time import sleep
from app.models import reglink

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from app.models.reglink import Reglink


@shared_task()
def sendreglink(reglink_id):
    reglink = Reglink.objects.get(pk=reglink_id)
    namesubject = ("Registration Link for " + str(reglink.lead_mail))
    details = ("http://localhost:8000/leadactivation/"+ str(reglink.lead_reglink))
    email = str(reglink.lead_mail)
    send_mail(
        subject=namesubject,
        message=details,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_HOST_USER],
        fail_silently=True,
    )
