from django.conf import settings
from django.db import models
from hashid_field import HashidAutoField
from django_fsm import FSMField, transition
from app.models.client import Client

class Project(models.Model):
    
    id = HashidAutoField(
        primary_key=True, salt=f"projectmodel{settings.HASHID_FIELD_SALT}"
    )
    name = models.CharField(max_length=150, blank=True, null=True)
    state = FSMField(default="new", protected=True)
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="client_profile"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    @transition(field=state, source="new", target=" in-progress")
    def progress(self):
        return "new to progress"

    @transition(field=state, source="progress", target="done")
    def done(self):
        return "progress to done"

    @transition(field=state, source="progress", target="terminated")
    def terminated(self):
        return "progress to terminated"