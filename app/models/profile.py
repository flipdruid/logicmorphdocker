from django.conf import settings
from hashid_field import HashidAutoField
from datetime import datetime
from django.db import models
from accounts.models import User
import os, random


def image_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    randomstr =''.join((random.choice(chars)) for x in range(10))
    _now = datetime.now()

    return 'avatar/{year}-{month}-{day}-{imageid}-{basename}-{randomstring}{ext}'.format(imageid = instance,
                                                                                        basename=basefilename,
                                                                                        randomstring=randomstr,
                                                                                        ext=file_extension,
                                                                                        year=_now.strftime('%Y'),
                                                                                        month=_now.strftime('%m'),
                                                                                        day=_now.strftime('%d'))



class Profile(models.Model):
    id                  =       HashidAutoField(primary_key=True, salt=f"profilemodel{settings.HASHID_FIELD_SALT}")
    user                =       models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile")
    avatar              =       models.ImageField(upload_to=image_path, default='avatar/lmlt.png')
    is_logicmorph_staff =       models.BooleanField(default=False)
    is_dark_theme       =       models.BooleanField(default=False)

