from django import forms
from .models import Album, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =[
            'comment',
            'name',
        ]