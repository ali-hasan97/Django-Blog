from django import forms
from . models import Category, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'content']

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'content']