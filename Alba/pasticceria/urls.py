from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [  
    path('',views.index, name='index'),
    path('clienteAlta', views.clienteAlta, name='clienteAlta'),
    path('clienteListar', views.clienteListar, name='clienteListar'),
    path('cliente/actualizar/<int:pk>', views.clienteActualizar, name='clienteActualizar'),
    path('cliente/borrar/<int:pk>', views.clienteBorrar, name='clienteBorrar'),
    # path('menu', views.menu, name='menu'),
    # path('cafe', views.cafe, name='cafe'),
    # path('abmProductos', views.abmProductos, name='abmProductos'),
    # path('admin', views.admin, name='admin'),
    path('crear_orden/', views.crear_orden, name='crear_orden'),
    path('anadir_orden_items/<int:orden_id>/', views.anadir_orden_items, name='anadir_orden_items'),
    path('ordenItemEditar/<int:orden_id> <int:item_id>/', views.ordenItemEditar, name='ordenItemEditar'),
    path('ordenItemBorrar/<int:orden_id> <int:item_id>/', views.ordenItemBorrar, name='ordenItemBorrar'),
    
    path('productoAlta', views.ProductoCreateView.as_view(), name='productoAlta'),
    path('productoListar', views.ProductoListView.as_view(), name='productoListar'),
    # path('productoAlta/<int:pk>', views.ProductoUpdateView.as_view(), name='productoActualizar'),
    path('productoActualizar/<int:pk>', views.ProductoUpdateView.as_view(), name='productoActualizar'),
    path('productoBorrar/<int:pk>', views.ProductoDeleteView.as_view(), name='productoBorrar'),
    
    path('restricted/', views.restricted, name='restricted'),
]
