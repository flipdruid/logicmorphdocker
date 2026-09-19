import os
import random
from datetime import datetime
from django.utils.safestring import mark_safe
from django.conf import settings
from django.db import models
from hashid_field import HashidAutoField

from accounts.models import User
randomstr=""

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

def default_avatar():
    return "avatar/logicmorph" + random.choice("0123456789") + ".png"


class Profile(models.Model):
    id = HashidAutoField(
        primary_key=True, salt=f"profilemodel{settings.HASHID_FIELD_SALT}"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile_user")
    avatar = models.ImageField(upload_to=image_path, default=default_avatar)
    is_logicmorph_staff = models.BooleanField(default=False)
    is_dark_theme = models.BooleanField(default=False)

    def image_tagfront(self):
        return mark_safe('<img src="/app/media/%s" width="50" height"50" />'%(self.avatar))
    
    def __str__(self):
        return str(self.user)
