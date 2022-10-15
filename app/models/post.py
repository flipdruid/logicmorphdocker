from django.conf import settings
from hashid_field import HashidAutoField
from django.db import models
from accounts.models import User



class Post(models.Model):
    id              =   HashidAutoField(primary_key=True, salt=f"postmodel{settings.HASHID_FIELD_SALT}") 
    title           =   models.CharField(max_length = 150)
    description     =   models.TextField (max_length = 500)
    created_by      =   models.ForeignKey(User, on_delete=models.CASCADE, related_name ="post")
    created_at      =   models.DateTimeField(auto_now_add = True)
    updated_at      =   models.DateTimeField(auto_now_add=True)


    class Meta:
       ordering = ['-created_at']
