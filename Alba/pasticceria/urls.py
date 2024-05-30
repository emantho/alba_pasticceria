from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('abm_clients', views.abm_clients, name='abm_clients'),
    path('menu', views.menu, name='menu'),
    path('cafe', views.cafe, name='cafe'),
    path('abmProductos', views.abmProductos, name='abmProductos'),
    path('admin', views.admin, name='admin'),
]
