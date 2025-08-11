from django import forms
from django.contrib.auth.forms import UserCreationForm,UsernameField,PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation

class MyPasswordchangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Old Password", strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control'}))
    new_password1 = forms.CharField(label=("New password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),
    help_text=password_validation.password_validators_help_text_html())
    new_password2 =forms.CharField(label=("Confirm New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))