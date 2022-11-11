
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Submit

from django.forms import ModelForm
from app.models.profile import Profile


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        # fields = "__all__"
        fields = ["avatar", "is_dark_theme"]
    # @property
    # def helper(self):
    #     helper = FormHelper()
    #     helper.layout = Layout(
    #         HTML("Something"),
    #         Field("avatar"),
    #         Field("is_logicmorph_staff"),
    #         Field("is_dark_theme"),

    #     )
    #     for field in self.Meta().fields:
    #         helper.layout.append (
    #             Field(field, wrapper_class = "row")
    #         )
    #     helper.layout.append(Submit("submit", "Submit your changes", 
    #     css_class="btn-success"))
    #     helper.field_class = "col-9"
    #     helper.label_class = "col-3"
    #     return helper

