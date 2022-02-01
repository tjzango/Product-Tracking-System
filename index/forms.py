from dataclasses import field
from unicodedata import name
from django import forms
from .models import Product
from django.contrib.auth.models import User


class ItemForm(forms.ModelForm):
    serial_number = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': "form-control"}))
    class Meta:
        model = Product
        fields = ("serial_number",)



class UserForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'haroun@gmail.com'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': '*******'}))
