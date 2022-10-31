from django import forms
from app.models.client import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
