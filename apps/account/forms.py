from django import forms
from project.libs.constants import GENDER_CHOICES

class VerifyCredentialsAccountForm(forms.Form):
    username        = forms.CharField()
    password        = forms.CharField()

class UpdateProfileAccountForm(forms.Form):
    birthday        = forms.DateField()
    gender          = forms.ChoiceField()

class UpdateProfileImageAccountForm(forms.Form):
    birthday        = forms.DateField()
    gender          = forms.ChoiceField(choices=GENDER_CHOICES)

class ReadSettingsAccountForm(forms.Form):
    id              = forms.DateField()

class UpdateSettingsAccountForm(forms.Form):
    id              = forms.DateField()