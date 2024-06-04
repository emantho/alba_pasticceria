from django.db import models
from datetime import date

# Create your models here.
class cliente(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    dni = models.IntegerField(verbose_name="DNI", unique= True)
    email = models.EmailField(max_length=254, verbose_name="Email", unique= True)
    direccion = models.CharField(max_length=100, verbose_name ="Dirección")
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad")
    cumpleaños = models.DateField(("Date"), default=date.today)