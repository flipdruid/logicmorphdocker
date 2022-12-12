from __future__ import absolute_import
import celery
import random
from django.conf import settings
from django.db import models
from hashid_field import HashidAutoField

# chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
# randomstr = "".join((random.choice(chars)) for x in range(30))


class Reglink(models.Model):
    id = HashidAutoField(
        primary_key=True, salt=f"reglinksrmodel{settings.HASHID_FIELD_SALT}"
    )
    lead_firstname = models.CharField(max_length=50, verbose_name="First Name")
    lead_lastname = models.CharField(max_length=50, verbose_name="Last Name")
    lead_mail = models.EmailField(max_length=50, verbose_name="Lead Email")
    lead_id   = models.CharField(max_length=50, verbose_name="Lead ID")
    lead_reglink   = models.CharField(max_length=150, verbose_name="Lead Registration Link")
    link_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return str(self.lead_mail)

    # def save(self, *args, **kwargs):
    #     super(Reglink, self).save(*args, **kwargs)
    #     celery.current_app.send_task(
    #         "app.tasks.leadtoclient_sendreglink.sendreglink", args=(str(self.id),)
    #     )
