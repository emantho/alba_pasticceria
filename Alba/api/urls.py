from django.contrib import admin
from django.urls import path, include
from api import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clientes', views.ClienteViewSet, basename='cliente'),
router.register(r'productos', views.ProductoViewSet, basename='producto'),
router.register(r'vendedores', views.VendedorViewSet, basename='vendedor'),
router.register(r'ordenes', views.OrdenViewSet, basename='orden'),
router.register(r'ordenItems', views.OrdenItemViewSet, basename='ordenItems'),


urlpatterns = [    
    path("", include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]
