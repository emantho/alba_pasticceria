from django import forms
from django.core.exceptions import ValidationError
from .models import Orden, OrdenItem, Producto
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


class ProductosForm(forms.ModelForm):
    listaCategorias = [
        (1, "Cafeteria"),
        (2, "Postres"),
        (3, "Tortas"),
        (4, "Bebidas Calientes"),
        (5, "Bebidas Frias")
    ]
    categorias = forms.ChoiceField(choices=listaCategorias)

    class Meta:
        model = Producto
        fields = [
            "codigo",
            "nombre",
            "descripcion",
            "categorias",
            "precio",
            "existencias",
        ]
        labels = {
            "codigo": "Código",
            "nombre": "Nombre",
            "descripcion": "Descripción",
            "precio": "Precio",
            "existencias": "Existencias",
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if not nombre.isalpha():
            raise ValidationError("Name can only contains letters")
        return nombre

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
    
    def clean(self):
        cleaned_data = super().clean()
        producto = cleaned_data.get('producto')
        cantidad = cleaned_data.get('cantidad')
        if producto and cantidad:
            cleaned_data['total'] = 100
            return cleaned_data
