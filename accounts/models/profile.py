from django.db import models

from django.db import models
from accounts.models.user import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username