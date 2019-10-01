from django import forms
from .models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields = ('article', 'message', 'name', 'email','website')