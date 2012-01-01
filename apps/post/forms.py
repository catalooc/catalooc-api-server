from django import forms

class UserTimelineForm(forms.Form):
    id          = forms.CharField()

class DestroyPostForm(forms.Form):
    id          = forms.CharField()

class CreatePostForm(forms.Form):
    title       = forms.CharField(max_length=64, required=False)
    description = forms.CharField(required=False)
    lat         = forms.FloatField()
    lon         = forms.FloatField()