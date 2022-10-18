from datetime import datetime

from django.conf import settings
from django.db import models
from hashid_field import HashidAutoField

from app.models import Client


class Project(models.Model):
    id = HashidAutoField(
        primary_key=True, salt=f"projectmodel{settings.HASHID_FIELD_SALT}"
    )
    name = models.CharField(max_length=150)
    state = models.CharField(max_length=30)
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="client_profile"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
