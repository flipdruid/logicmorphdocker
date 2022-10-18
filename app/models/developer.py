from django.conf import settings
from hashid_field import HashidAutoField
from django.db import models
from app.models import Project, Profile
import os, random

class Developer(models.Model):
    id                  =   HashidAutoField(primary_key=True, salt=f"developermodel{settings.HASHID_FIELD_SALT}")
    project             =   models.ForeignKey(Project, on_delete=models.CASCADE, related_name ="developer_project")
    profile             =   models.ForeignKey(Profile, on_delete=models.CASCADE, related_name ="developer_profile")
    role                =   models.CharField (max_length = 200)
    state               =   models.CharField (max_length = 200)