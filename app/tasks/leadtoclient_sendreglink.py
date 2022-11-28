from __future__ import absolute_import
from django.template.loader import render_to_string
from django.utils.html import strip_tags, format_html
from django.contrib.sites.models import Site

from time import sleep
from app.models import reglink

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage

from app.models.reglink import Reglink


@shared_task()
def sendreglink(reglink_id):
    reglink = Reglink.objects.get(pk=reglink_id)
    namesubject = ("Registration Link for " + str(reglink.lead_mail))
    details = (str(Site.objects.get_current())+"/portal/leadactivation/"+ str(reglink.lead_reglink))
    html_content = render_to_string("main/email_template.html", {'details' : details, 'fname':reglink.lead_firstname})
    # html_content = "<p>" + details + "</p>"
    # html_content = strip_tags(html_content)
    email = str(reglink.lead_mail)
    send_mail(
        subject=namesubject,
        message=html_content,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_HOST_USER],
        html_message=html_content
        # fail_silently=True,
    )
    # sendMail=EmailMultiAlternatives(
    #     namesubject,
    #     html_content,
    #     settings.EMAIL_HOST_USER,
    #     settings.EMAIL_HOST_USER,
    # )
    # sendMail.attach_alternative(html_content, "text/html")
    # sendMail.content_subtype = "html" 
    # sendMail.send()
