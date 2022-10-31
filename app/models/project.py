from datetime import datetime
from email.policy import default

from django.conf import settings
from django.db import models
from hashid_field import HashidAutoField
from django_fsm import FSMField, transition
from app.models.client import Client


class Project(models.Model):
    
    id = HashidAutoField(
        primary_key=True, salt=f"projectmodel{settings.HASHID_FIELD_SALT}"
    )
    name = models.CharField(max_length=150, default="Project Name")
    # state = models.CharField(max_length=30)
    state = FSMField(default="new", protected=True)
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="client_profile"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    @transition(field=state, source="new", target="partnered")
    def partnered(self):
        pass
