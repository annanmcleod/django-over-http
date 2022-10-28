from django import forms

class NearForm(forms.Form):
    n = forms.IntegerField()


class StringForm(forms.Form):
    str = forms.CharField()


class CatForm(forms.Form):
    str = forms.CharField()


class LoneForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    c = forms.IntegerField()