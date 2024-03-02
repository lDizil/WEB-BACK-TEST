from .models import Data
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class DataForm(ModelForm):
    class Meta:
        model = Data
        fields = ['Login', 'Status', 'About', 'Date']

        widgets = {
            "Login": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин'
            }),
            "Status": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Статус'
            }),
            "About": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'О домашних поросях'
            }),
            'Date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата регистрации'
            }),
        }