from django import forms
from martor.fields import MartorFormField

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            'title',
            'body',
        )


