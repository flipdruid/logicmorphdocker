from django.conf import settings
from django.db import models
from hashid_field import HashidAutoField

class Appsetting(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    id = HashidAutoField(
        primary_key=True, salt=f"lmthememodel{settings.HASHID_FIELD_SALT}"
    )
    is_dark_theme = models.BooleanField(default=False)
    name = models.CharField(max_length=50, verbose_name="Name")