from email.policy import default
import os
import random
from datetime import datetime

from django.conf import settings
from django.db import models

from hashid_field import HashidAutoField
from app.models.profile import Profile


def image_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    randomstr = "".join((random.choice(chars)) for x in range(10))
    _now = datetime.now()

    return (
        "avatar/{year}-{month}-{day}-{imageid}-{basename}-{randomstring}{ext}".format(
            imageid=instance,
            basename=basefilename,
            randomstring=randomstr,
            ext=file_extension,
            year=_now.strftime("%Y"),
            month=_now.strftime("%m"),
            day=_now.strftime("%d"),
        )
    )


class Client(models.Model):
    id = HashidAutoField(
        primary_key=True, salt=f"clientmodel{settings.HASHID_FIELD_SALT}"
    )
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="profile_client"
    )
    business_name = models.CharField(max_length=150, blank=True, null=True)
    business_logo = models.ImageField(
        upload_to=image_path, default="business_logo/lmlt.png"
    )
    address = models.CharField(max_length=200, blank=True, null=True)
    telephone_no = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.profile)
