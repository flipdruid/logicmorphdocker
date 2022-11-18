from __future__ import absolute_import
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from time import sleep

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from app.models.lead import Lead


@shared_task()
def contactuser_sendmail(customer_id):
    try:
        lead = Lead.objects.get(pk=customer_id)
        namesubject = (
            str(lead.entity_name)
            + " |"
            + str(lead.first_name)
            + " "
            + str(lead.last_name)
            + "| Client ID:"
            + str(lead.id)
            + "| Sender: "
            + str(lead.email)
        )
        details = (
            str(lead.details)
            + "\n\n Created at: "
            + str(lead.created_at)
            + "\n Updated at:"
            + str(lead.updated_at)
        )
        email = str(lead.email)
        send_mail(
            subject=namesubject,
            message=details,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=True,
        )
    except ObjectDoesNotExist:
        pass