from django.conf import settings
from django.db import models
from hashid_field import HashidAutoField

from accounts.models.user import User


class Profile(models.Model):
    id = HashidAutoField(
        primary_key=True, salt=f"profilemodel{settings.HASHID_FIELD_SALT}"
    )
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_profile"
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
