
from django.db import models
 

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