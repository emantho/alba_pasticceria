from django import forms

class AbmClientsForm(forms.Form):
    userName = forms.CharField(label='First Name', required=True)
    lastName = forms.CharField(label='Last Name', required=True)
    dni = forms.IntegerField(label="DNI", required=True)
    email = forms.EmailField(label="Email", required=True)