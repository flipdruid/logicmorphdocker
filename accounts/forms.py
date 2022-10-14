from dataclasses import fields
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm

from django import forms

from accounts.models import User, Customer

class UserForm (UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model   =   User
        fields  =    ('email', 'username','first_name', 'last_name', 'password1', 'password2')


class CustomerForm(forms.ModelForm):
    class Meta:
        model   =   Customer
        fields  =   '__all__'

        # widgets = {
        #     'first_name': forms.TextInput(attrs={'class': 'form-control', 
        #                     'id':'first_name', 
        #                     'placeholder': 'First Name',
        #                     "required": True}),
        #     'last_name' : forms.TextInput(attrs={'class': 'form-control', 
        #                     'id': 'last_name', 
        #                     'placeholder': 'lirst Name',
        #                     "required": True}),
        #     'email' : forms.EmailInput(attrs={'class': 'form-control', 
        #                     'id': 'email', 
        #                     'placeholder': 'Email',
        #                     "required": True}),
        #     'entity_name' : forms.TextInput(attrs={'class': 'form-control', 
        #                     'id': 'entity_name', 
        #                     'placeholder': 'Subject',
        #                     "required": True}),
        #     'details' : forms.Textarea(attrs={'class': 'form-control', 
        #                     'id': 'details', 
        #                     'placeholder': 'Details',
        #                     "required": True})
            
        # }