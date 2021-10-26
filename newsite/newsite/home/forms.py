from django import forms
from django.forms import fields, widgets
from .models import Entries

class PostForm(forms.ModelForm):
    class Meta:
        model = Entries
        fields = ('title', 'text', 'author')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'text' : forms.Textarea(attrs={'class':'form-control'}),
            'author' : forms.Select(attrs={'class':'form-control'}),
        }