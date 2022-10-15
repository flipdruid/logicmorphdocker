from django.conf import settings
from hashid_field import HashidAutoField
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id                  =   HashidAutoField(primary_key=True, salt=f"postmodel{settings.HASHID_FIELD_SALT}")
    email               =   models.EmailField(unique=True)
    USERNAME_FIELD      =   "email"
    REQUIRED_FIELDS     =   ["username", "first_name",'last_name']

    def __str__(self):
        return self.email