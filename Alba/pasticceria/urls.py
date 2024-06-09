from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('clienteAlta', views.clienteAlta, name='clienteAlta'),
    path('clienteListar', views.clienteListar, name='clienteListar'),
    path('menu', views.menu, name='menu'),
    path('cafe', views.cafe, name='cafe'),
    path('abmProductos', views.abmProductos, name='abmProductos'),
    path('admin', views.admin, name='admin'),
    path('crear_orden/', views.crear_orden, name='crear_orden'),
    path('anadir_orden_items/<int:orden_id>/', views.anadir_orden_items, name='anadir_orden_items'),
]
