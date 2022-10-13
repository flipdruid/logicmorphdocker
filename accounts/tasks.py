from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from django.conf import settings
@shared_task(bind=True)
def contact_us_mail(self=None, namesubject=None, details=None,  email=None):
    send_mail (
        subject=namesubject,
        message=details,
        from_email=email,
        recipient_list=['philip.logicmorph@gmail.com'],
        fail_silently=True
    )
    return "Done"