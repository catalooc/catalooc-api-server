from django import forms

class CreateFavoritesForm(forms.Form):
    id      = forms.CharField()
    why     = forms.CharField(required=False)
    lat     = forms.FloatField()
    lon     = forms.FloatField()

class DestroyFavoritesForm(forms.Form):
    id      = forms.CharField()