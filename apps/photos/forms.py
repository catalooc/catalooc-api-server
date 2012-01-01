from django import forms

class ShowPhotosForm(forms.Form):
    id      = forms.CharField()

class CreatePhotosForm(forms.Form):
    caption = forms.CharField()
    photo   = forms.ImageField()
    lat     = forms.FloatField()
    lon     = forms.FloatField()

class DestroyPhotosForm(forms.Form):
    id      = forms.CharField()