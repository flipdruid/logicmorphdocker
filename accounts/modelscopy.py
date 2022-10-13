import email
from ssl import create_default_context
from statistics import mode
from tabnanny import verbose
from xml.sax import default_parser_list
from django.db import models
from django.contrib.auth.models import AbstractUser
# from accounts.tasks import contact_us_send_mail


class User(AbstractUser):
    email       =   models.EmailField(unique=True)
    USERNAME_FIELD  =   "email"
    REQUIRED_FIELDS =   ["username", "first_name",'last_name']

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Customer(models.Model):
    first_name  =   models.CharField(max_length=50, verbose_name = "First Name")
    last_name   =   models.CharField(max_length=50, verbose_name = "Last Name")
    email       =   models.EmailField(max_length=50)
    entity_name =   models.CharField(max_length=100, verbose_name = "Subject")
    details     =   models.TextField()
    created_at  =   models.DateTimeField(auto_now_add=True)
    updated_at  =   models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    def save (self,*args, **kwargs):
        super (Customer, self).save(*args, **kwargs)
        contact_us_send_mail.delay(self.id)



    