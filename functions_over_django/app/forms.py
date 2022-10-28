from django import forms

class AddForm(forms.Form):
    x = forms.IntegerField()
    y = forms.IntegerField()

class HeyForm(forms.Form):
    name = forms.CharField()

class AgeForm(forms.Form):
    death = forms.IntegerField()
    birth = forms.IntegerField()

class OrderForm(forms.Form):
    bt = forms.IntegerField()
    ft = forms.IntegerField()
    dt = forms.IntegerField()