from django.contrib import admin
from .models import Cliente, Vendedor, Producto, Orden, OrdenItem

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Producto)
admin.site.register(Orden)
admin.site.register(OrdenItem)