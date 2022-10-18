from django.conf import settings
from hashid_field import HashidAutoField
from django.db import models
import os, random
from datetime import datetime


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

class Client(models.Model):
    id              =   HashidAutoField(primary_key=True, salt=f"clientmodel{settings.HASHID_FIELD_SALT}") 
    business_name   =   models.CharField(max_length = 150)
    business_logo   =   models.ImageField(upload_to=image_path, default='business_logo/lmlt.png')
    address         =   models.CharField (max_length = 200)
    telephone_no    =   models.IntegerField()
    position        =   models.CharField(max_length = 100)

