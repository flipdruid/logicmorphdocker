from django import forms
from app.models import Lead

class PostForm(forms.modelForm):
    class Meta:
        model   =   Lead
        fields  =   '__all__'