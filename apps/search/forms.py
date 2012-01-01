from django import forms

class FindSearchForm(forms.Form):
    query       = forms.CharField()
    lat         = forms.FloatField()
    lon         = forms.FloatField()

class UsersSearchForm(forms.Form):
    username    = forms.CharField()
    lat         = forms.FloatField()
    lon         = forms.FloatField()