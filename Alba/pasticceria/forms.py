from typing import Any
from django import forms
from django.core.exceptions import ValidationError


class AbmClientsForm(forms.Form):
    firstName = forms.CharField(label='Nombre', required=True)#, widget=forms.TextInput(attrs={'class':'blue_field'})
    lastName = forms.CharField(label='Apellido', required=True)
    dni = forms.IntegerField(label="DNI", required=True)
    telephone = forms.CharField(label="Telefono", required=True)
    address = forms.CharField(label="Dirección",required=True)
    city = forms.CharField(label="Ciudad",required=True)
    zip = forms.CharField(label="Código Postal",required=True)
    CHOICES = [
        ('1','Cuenta Personal'),
        ('2','Cuenta Empresa'),  
    ] 
    Cuenta = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    birthday = forms.DateField(label="Fecha de Nacimiento", widget=forms.SelectDateWidget)
    optionList = [(1,"Facebook"),(2,"Instagram"),(3,"Tiktok"),(4,"Snapchat"),(5,"TV"),(6,"Radio"),(7,"Otro")]
    hearFromUs = forms.CharField(label="¿Como nos conociste?", widget=forms.Select(choices=optionList))
    # comment = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
    
    def clean_userName(self):
        if not self.cleaned_data["firstName"].isalpha():
            raise ValidationError("Name can only contains letters")            
        
        return self.cleaned_data["firstName"]
    
    def clean_lastName(self):
        if not self.cleaned_data["lastName"].isalpha():
            raise ValidationError("Name can only contains letters")            
        
        return self.cleaned_data["lastName"]
    
    def clean(self):
        cleaned_data = super().clean()
        firstName = cleaned_data.get("firstName")
        lastName = cleaned_data.get("lastName")
        if firstName == "Carlos" and lastName == "Lopez":
            raise ValidationError("User already exists")
        
        # if self.cleaned_data["dni"] < 1000000:
        #     raise ValidationError("The DNI must have less than eight (8) digits")
        
        return self.cleaned_data


class AbmProductosForm(forms.Form):
    nombreProducto = forms.CharField(label='Nombre', required=True)#, widget=forms.TextInput(attrs={'class':'blue_field'})
    descripcion = forms.CharField(label='Descripción', required=True)
    
    listaCategorias = [(1,"Facebook"),(2,"Instagram"),(3,"Tiktok"),(4,"Snapchat"),(5,"TV"),(6,"Radio"),(7,"Otro")]
    categorias = forms.CharField(label="Categorias", widget=forms.Select(choices=listaCategorias))
    precio = forms.CharField(label="Precio", required=True)
    rating = forms.CharField(label="Rating",required=True)
    cantidadDisponible = forms.CharField(label="Cantidad Disponible",required=True)
    
    def clean_userName(self):
        if not self.cleaned_data["firstName"].isalpha():
            raise ValidationError("Name can only contains letters")            
    
        return self.cleaned_data["firstName"]
    
    def clean_lastName(self):
        if not self.cleaned_data["lastName"].isalpha():
            raise ValidationError("Name can only contains letters")            
        
        return self.cleaned_data["lastName"]
    
    def clean(self):
        cleaned_data = super().clean()
        firstName = cleaned_data.get("firstName")
        lastName = cleaned_data.get("lastName")
        if firstName == "Carlos" and lastName == "Lopez":
            raise ValidationError("User already exists")
        
        # if self.cleaned_data["dni"] < 1000000:
        #     raise ValidationError("The DNI must have less than eight (8) digits")
        
        return self.cleaned_data
