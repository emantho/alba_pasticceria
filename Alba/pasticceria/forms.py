from typing import Any
from django import forms
from django.core.exceptions import ValidationError


class AbmClientsForm(forms.Form):
    userName = forms.CharField(label='First Name', required=True, widget=forms.TextInput(attrs={'class':'blue_field'}))
    lastName = forms.CharField(label='Last Name', required=True)
    dni = forms.IntegerField(label="DNI", required=True)
    email = forms.EmailField(label="Email", required=True)
    
    def clean_userName(self):
        if not self.cleaned_data["userName"].isalpha():
            raise ValidationError("Name can only contains letters")            
        
        return self.cleaned_data["userName"]
    
    def clean_lastName(self):
        if not self.cleaned_data["lastName"].isalpha():
            raise ValidationError("Name can only contains letters")            
        
        return self.cleaned_data["lastName"]
    
    def clean(self):
        cleaned_data = super().clean()
        userName = cleaned_data.get("userName")
        lastName = cleaned_data.get("lastName")
        if userName == "Carlos" and lastName == "Lopez":
            raise ValidationError("User already exists")
        
        # if self.cleaned_data["dni"] < 1000000:
        #     raise ValidationError("The DNI must have less than eight (8) digits")
        
        return self.cleaned_data
        

