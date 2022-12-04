
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Submit

from django.forms import ModelForm, TextInput, DateField, ImageField, FileInput
from app.models.profile import Profile


class ProfileUpdateForm(ModelForm):
    avatar = ImageField(widget=FileInput)
    class Meta:
        model = Profile
        fields = ["avatar", "is_dark_theme","is_logicmorph_staff"]

class ProfileViewForm(ModelForm):
    # avatar = DateField(widget=FileInput)
    # is_dark_theme = DateField(widget=TextInput, disabled=True)
    # is_logicmorph_staff = DateField(widget=TextInput, disabled=True)
    class Meta:
        model = Profile
        fields = ["is_dark_theme","is_logicmorph_staff"]

class ProfileViewClient(ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar"]