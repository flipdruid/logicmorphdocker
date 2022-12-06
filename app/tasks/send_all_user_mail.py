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
from django.contrib.auth import get_user_model


@shared_task()
def send_all_user_mail():
    users = get_user_model().objects.all()
    for user in users :
        namesubject = "Testing Celery Beat " + user.email
        html_content = "Testing Celery Beat Content " + user.email        
        send_mail(
            subject=namesubject,
            message=html_content,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            html_message=html_content
        )