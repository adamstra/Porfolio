from django import forms
from .models import contactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = contactModel
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.TextInput(attrs={'class': 'form-control'})
        }
