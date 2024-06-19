from django.shortcuts import render
from rest_framework import viewsets, permissions
from api.serializers import ClienteSerializer, ProductoSerializer, VendedorSerializer, OrdenSerializer, OrdenItemSerializer
from pasticceria.models import Cliente, Producto, Vendedor, Orden, OrdenItem

# Create your views here.

## ------- CLIENTE API ---------------------------------------------------------------  
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class OrdenItemViewSet(viewsets.ModelViewSet):
    queryset = OrdenItem.objects.all()
    serializer_class = OrdenItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]