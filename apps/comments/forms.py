from django import forms

class CreateCommentsForm(forms.Form):
    comment = forms.CharField()
    lat     = forms.FloatField()
    lon     = forms.FloatField()

class DestroyCommentsForm(forms.Form):
    id      = forms.CharField()

class LockCommentsForm(forms.Form):
    id      = forms.CharField()

class UnlockCommentsForm(forms.Form):
    id      = forms.CharField()