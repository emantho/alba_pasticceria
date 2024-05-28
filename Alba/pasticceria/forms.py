from typing import Any
from django import forms
from django.core.exceptions import ValidationError


class AbmClientsForm(forms.Form):
    userName = forms.CharField(label='Nombre', required=True)#, widget=forms.TextInput(attrs={'class':'blue_field'})
    lastName = forms.CharField(label='Apellido', required=True)
    dni = forms.IntegerField(label="DNI", required=True)
    email = forms.EmailField(label="Email", required=True)
    password = forms.CharField(label="Contraseña",required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    CHOICES = [
        ('1','Cuenta Personal'),
        ('2','Cuenta Empresa'),  
    ] 
    Cuenta= forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    birthday = forms.DateField(label="Fecha de Nacimiento", widget=forms.SelectDateWidget)
    optionList = [(1,"Facebook"),(2,"Instagram"),(3,"Tiktok"),(4,"Snapchat"),(5,"TV"),(6,"Radio"),(7,"Otro")]
    hearFromUs = forms.CharField(label="¿Como nos conociste?", widget=forms.Select(choices=optionList))
    comment = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
    
    

    
    
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



