from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User


class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "email",
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )

class UserUpdateForm (forms.ModelForm):
    class Meta:
        model = User
        fields= (
            "username",
            "first_name",
            "last_name",
        )