from django import forms

class CreateFollowersForm(forms.Form):
    id      = forms.CharField()
    lat     = forms.FloatField()
    lon     = forms.FloatField()

class DestroyFollowersForm(forms.Form):
    id      = forms.CharField()