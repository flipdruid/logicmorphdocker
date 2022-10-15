from __future__ import absolute_import
from django.conf import settings
from hashid_field import HashidAutoField
from django.db import models
import celery

class Lead(models.Model):
    id          =   HashidAutoField(primary_key=True, salt=f"leadmodel{settings.HASHID_FIELD_SALT}")
    first_name  =   models.CharField(max_length=50, verbose_name = "First Name")
    last_name   =   models.CharField(max_length=50, verbose_name = "Last Name")
    email       =   models.EmailField(max_length=50)
    entity_name =   models.CharField(max_length=100, verbose_name = "Subject")
    details     =   models.TextField()
    created_at  =   models.DateTimeField(auto_now_add=True)
    updated_at  =   models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):        
        super(Lead, self).save(*args, **kwargs)
        celery.current_app.send_task('app.tasks.contactuser_sendmail.contactuser_sendmail', args=(str(self.id),))
        
  

