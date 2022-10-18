from dataclasses import fields

from django import forms

from app.models import Post


class PostForm(forms.modelForm):
    class Meta:
        model = Post
        fields = "__all__"
