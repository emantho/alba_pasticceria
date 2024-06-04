from django import forms
from django.core.exceptions import ValidationError
import datetime


class AbmClientsForm(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True, widget=(forms.TextInput(attrs={"":""})))
    apellido = forms.CharField(label='Apellido', required=True)
    dni = forms.IntegerField(label="DNI", required=True)
    telefono = forms.CharField(label="Telefono")
    email = forms.EmailField(label="Email",required=True)
    direccion = forms.CharField(label="Dirección",required=True)
    ciudad = forms.CharField(label="Ciudad",required=True)
    anios = range(1900, datetime.datetime.now().year + 1)
    cumpleanios = forms.DateField(label="Fecha de Nacimiento", widget=forms.SelectDateWidget(years=anios), )
    
    def clean_firstName(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError("El nombre solo puede contener letras")            
        
        return self.cleaned_data["nombre"]
    
    def clean_lastName(self):
        if not self.cleaned_data["apellido"].isalpha():
            raise ValidationError("El apellido solo puede contener letras")            
        
        return self.cleaned_data["apellido"]
    
    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")
        apellido = cleaned_data.get("apellido")
        if nombre == "Carlos" and apellido == "Lopez":
            raise ValidationError("El Cliente ya existe en el sistema")
        
        return cleaned_data


class AbmProductosForm(forms.Form):
    nombreProducto = forms.CharField(label='Nombre', required=True)
    descripcion = forms.CharField(label='Descripción', required=True)
    
    listaCategorias = [(1,"Facebook"),(2,"Instagram"),(3,"Tiktok"),(4,"Snapchat"),(5,"TV"),(6,"Radio"),(7,"Otro")]
    categorias = forms.CharField(label="Categorias", widget=forms.Select(choices=listaCategorias))
    precio = forms.IntegerField(label="Precio", required=True)
    rating = forms.CharField(label="Rating",required=True)
    cantidadDisponible = forms.IntegerField(
        label="Cantidad Disponible",
        required=True,
        initial=1,  # Set the default value here
    )
    
    def clean_nombreProducto(self):
        if not self.cleaned_data["nombreProducto"].isalpha():
            raise ValidationError("Name can only contains letters")            
    
        return self.cleaned_data["nombreProducto"]
    
    def clean_cantidadDisponible(self):
        cantidadDisponible = self.cleaned_data.get("cantidadDisponible")
        if cantidadDisponible <= 0:
            raise ValidationError("Cantidad no puede ser menor que cero (0)")
        return cantidadDisponible
    
    def clean(self):
        cleaned_data = super().clean()
        # Additional cleaning logic if needed
        return cleaned_data
