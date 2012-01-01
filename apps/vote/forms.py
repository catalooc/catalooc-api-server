from django import forms

class CreateVoteForm(forms.Form):
    id      = forms.CharField()
    lat     = forms.FloatField()
    lon     = forms.FloatField()

class DestroyVoteForm(forms.Form):
    id      = forms.CharField()