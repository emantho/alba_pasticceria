from rest_framework import serializers
from pasticceria.models import Cliente, Producto, Vendedor, Orden, OrdenItem

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['dni', 'nombre', 'apellido', 'email']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = "__all__"

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = "__all__"

class OrdenItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenItem
        fields = "__all__"