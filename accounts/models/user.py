import celery
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from hashid_field import HashidAutoField


class User(AbstractUser):
    id = HashidAutoField(
        primary_key=True, salt=f"abstractusermodel{settings.HASHID_FIELD_SALT}"
    )
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def __str__(self):
        return str(self.email)

    
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        celery.current_app.send_task(
            "app.tasks.contactuser_sendmail.contactuser_sendmail", args=(str(self.id),)
        )
