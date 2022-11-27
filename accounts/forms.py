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


class UserFormNoEmail(UserCreationForm):    

    def __init__(self, *args, **kwargs):
        super(UserFormNoEmail, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.HiddenInput()
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
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.HiddenInput()
    class Meta:
        model = User
        fields= (
            "username",
            "first_name",
            "last_name",
        )

class UserViewForm (forms.ModelForm):
    username = forms.DateField(widget=forms.TextInput, disabled=True)
    first_name = forms.DateField(widget=forms.TextInput, disabled=True)
    last_name = forms.DateField(widget=forms.TextInput, disabled=True)

    class Meta:
        model = User
        fields= (
            "username",
            "first_name",
            "last_name",
        )