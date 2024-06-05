from django.db import models
from datetime import date

# Create your models here.

# Relaciones
## relación 1 a 1 -> cliente  a Detalle
## relación 1 a n -> Vendedor a venta o producto ## 54:54 en modelos 2 
## relación n a n -> cliente  a producto

### models.ForeingKey(clase, on_delete=models.CASCADE, null=True)
### models.ManyToManyField(clase)

# Modelo datos
###
# Cliente
    # Nombre
    # Apellido
    # DNI
    
# Vendedor
    # Nombre
    # Apellido
    # DNI
    # Codigo
    
# Producto
    # Codigo
    # Nombre
    # inventario
    
# Venta <<<--- Conector x>x>x>x> Se puede cambiar el nombre a transacción
    # clienteID
    # productoID
    # cantidad
    # precio
    # vendedorID
    #### Ver video modelos 2 1:07:00
###

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    dni = models.IntegerField(verbose_name="DNI", unique= True)
    email = models.EmailField(max_length=254, verbose_name="Email", unique= True)
    direccion = models.CharField(max_length=100, verbose_name ="Dirección")
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad")
    cumpleaños = models.DateField(("Date"), default=date.today)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Vendedor(models.Model):
    codigo = models.IntegerField(verbose_name='Código', unique=True)
    nombre = models.CharField(verbose_name='Nombre', max_length=100)
    apellido = models.CharField(verbose_name='Apellido', max_length=100)
    dni = models.IntegerField(verbose_name='DNI', unique=True)

class Producto(models.Model):
    codigo = models.IntegerField(verbose_name='Código', unique=True)
    nombre = models.CharField(verbose_name='Nombre', max_length=100)
    descripcion = models.CharField(verbose_name='Descripción', max_length=100)
    categorias = models.CharField(verbose_name='Categorías', max_length=100, unique=True)
    precio = models.IntegerField(verbose_name='Precio')
    rating = models.CharField(verbose_name='Rating', max_length=100)
    inventario = models.IntegerField(verbose_name='Inventario')