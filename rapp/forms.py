from django import forms
from models import ToggleModel


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    fields = ['username', 'password']


class ToggleForm(forms.ModelForm):
    class Meta:
        model = ToggleModel
        fields = ['post']

# class RoomForm(forms.ModelForm):
#     class Meta:
#         model = RoomModel
#         fields = ['room']
#
#
# class ToggleForm(forms.ModelForm):
#     class Meta:
#         model = ToggleModel
#         fields = ['device']
