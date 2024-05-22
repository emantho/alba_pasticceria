from django import forms
from django.core.exceptions import ValidationError


class AbmClientsForm(forms.Form):
    userName = forms.CharField(label='First Name', required=True)
    lastName = forms.CharField(label='Last Name', required=True)
    dni = forms.IntegerField(label="DNI", required=True)
    email = forms.EmailField(label="Email", required=True)
    
    def clean_userName(self):
        if self.cleaned_data["userName"].isalpha():
            raise ValidationError("Name can only contains letters")            
        
        return self.cleaned_data["userName"]
    
    

