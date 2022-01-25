from django.forms import ModelForm
from django import forms
from .models import Blog


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'height', 'image', 'difficulty']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'difficulty': forms.Select(attrs={'class': 'form-control', 'selected': 'Выберите сложность...'}),
        }
