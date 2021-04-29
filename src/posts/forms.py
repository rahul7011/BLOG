from django import forms
from .models import Post,Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("__all__")

class CommentForm(forms.ModelForm):
    content=forms.CharField(widget=forms.Textarea(attrs={
        'rows':"4",
        'cols':"5",
    }))
    class Meta:
        model = Comment
        fields = ("content",)