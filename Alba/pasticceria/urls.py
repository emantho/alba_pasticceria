from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('client_list', views.client_list, name='client_list'),
    path('abm_clients', views.abm_clients, name='abm_clients'),
]
