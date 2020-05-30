from django import forms

class RegistrationForm(forms.Form):
		name = foms.CharField(max_length=50)
		email = forms.CharField(max_length=50)