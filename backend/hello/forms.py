from django import forms

class UserForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=20)
    age = forms.IntegerField(required=False, min_value=1, max_value=100)