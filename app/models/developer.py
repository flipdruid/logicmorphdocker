from django.conf import settings
from django.db import models
from hashid_field import HashidAutoField
from django_fsm import FSMField, transition
from app.models.profile import Profile
from app.models.project import Project



class Developer(models.Model):
    state = FSMField(default="new", protected=True)
    id = HashidAutoField(
        primary_key=True, salt=f"developermodel{settings.HASHID_FIELD_SALT}"
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="developer_project"
    )
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="developer_profile"
    )
    role = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

    @transition(field=state, source="new", target="regular")
    def regular(self):
        return "new to regular"