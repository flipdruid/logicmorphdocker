from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from django.conf import settings
from accounts.models import Customer



@shared_task(bind=True)
def contact_us_send_mail(self, customer_id):
    customer                =   Customer.objects.get(pk=customer_id)
    namesubject             =   str(customer.entity_name) + " |" + str(customer.first_name) + " " + str(customer.last_name) + "| Client ID:" + str(customer.id) + "| Sender: " + str(customer.email)
    details                 =   str(customer.details) + "\n\n Created at: " + str(customer.created_at) + "\n Updated at:" + str(customer.updated_at)
    email                   =   str(customer.email)
    send_mail (
        subject=namesubject,
        message=details,
        from_email=email,
        recipient_list=[settings.EMAIL_HOST_USER],
        fail_silently=True
    )
    