from django.contrib.auth.models import User
from .models import Dist
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class DistanceForm(forms.ModelForm):
    From = forms.CharField(widget=forms.TextInput)
    To = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Dist
        fields = ['From', 'To']

