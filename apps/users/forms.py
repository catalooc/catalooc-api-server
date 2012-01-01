from django import forms

class ShowUsersForm(forms.Form):
    id      = forms.CharField()