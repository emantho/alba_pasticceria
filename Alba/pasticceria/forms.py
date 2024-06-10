from django import forms
from django.core.exceptions import ValidationError
from .models import Orden, OrdenItem
import datetime


class ClienteAltaForm(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True, widget=(forms.TextInput(attrs={"":""})))
    apellido = forms.CharField(label='Apellido', required=True)
    dni = forms.IntegerField(label="DNI", required=True)
    telefono = forms.CharField(label="Telefono")
    email = forms.EmailField(label="Email",required=True)
    direccion = forms.CharField(label="Dirección",required=True)
    ciudad = forms.CharField(label="Ciudad",required=True)
    años = range(1900, datetime.datetime.now().year + 1)
    cumpleaños = forms.DateField(label="Fecha de Nacimiento", widget=forms.SelectDateWidget(years=años))
    
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
        # crear validaciones
        return cleaned_data


class AbmProductosForm(forms.Form):
    codigoProducto = forms.IntegerField(label='Código', required=True)
    nombreProducto = forms.CharField(label='Nombre', required=True)
    descripcion = forms.CharField(label='Descripción', required=True)
    
    listaCategorias = [(1,"Cafeteria"),(2,"Postres"),(3,"Tortas"),(4,"Bebidas Calientes"),(5,"Bebidas Frias")]
    categorias = forms.CharField(label="Categorias", widget=forms.Select(choices=listaCategorias), required=True)
    precio = forms.IntegerField(label="Precio", required=True)
    existencias = forms.IntegerField(
        label="Existencias",
        required=True,
        initial=1,  # default value in 1
    )
    
    def clean_nombreProducto(self):
        if not self.cleaned_data["nombreProducto"].isalpha():
            raise ValidationError("Name can only contains letters")            
    
        return self.cleaned_data["nombreProducto"]
    
    def clean_existencias(self):
        existencias = self.cleaned_data.get("existencias")
        if existencias <= 0:
            raise ValidationError("Cantidad no puede ser menor que cero (0)")
        return existencias
    
    def clean(self):
        cleaned_data = super().clean()
        # añadir más validaciones según requiera
        return cleaned_data

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['cliente', 'vendedor']

class OrdenItemForm(forms.ModelForm):
    class Meta:
        model = OrdenItem
        fields = ['producto', 'cantidad']



