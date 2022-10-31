from django import forms
from app.models.developer import Developer


class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = "__all__"
