from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Producto
from .models import Orden, OrdenItem, Producto, Cliente
from . import forms
from .forms import OrdenForm, OrdenItemForm, ProductosForm

# Create your views here.
def index(request):
    my_context_var = {
        "userName": "Visitante",
    }
    return render(request, "pasticceria/index.html", my_context_var)

## ------- CLIENTES --------------------------------------------------------
# Listar clientes
def clienteListar(request):
    clientes = Cliente.objects.all()
    return render(request, "pasticceria/clienteListar.html", {"clientes" : clientes})

# Alta de clientes
def clienteAlta(request):
    context = {}
    # crear un formulario en blanco
    if request == "GET":
        context["cliente_alta_form"] = forms.ClienteAltaForm()
    else:  
        form = forms.ClienteAltaForm(request.POST)
        context["cliente_alta_form"] = form
        # Validación de Formulario
        if form.is_valid():
            # SI correcto, guardar en DB, mostrar mensaje y redirigir
            cliente = Cliente(
                nombre = form.cleaned_data['nombre'],
                apellido = form.cleaned_data['apellido'],
                dni = form.cleaned_data['dni'],
                telefono = form.cleaned_data['telefono'],
                email = form.cleaned_data['email'],
                direccion = form.cleaned_data['direccion'],
                ciudad = form.cleaned_data['ciudad'],
                cumpleaños = form.cleaned_data['cumpleaños']
                )
            cliente.save()
            messages.success(request, "Cliente creado exitosamente")
            return redirect('clienteListar')
        # IF NO correct
        # else:            
        #     messages.error(request, "Existe un error, revise los datos ingresados")
    return render(request, "pasticceria/clienteAlta.html", {'form':form})

# Actualizar cliente
def clienteActualizar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = forms.ClienteAltaForm(request.POST)
        if form.is_valid():
            cliente.nombre = form.cleaned_data['nombre']
            cliente.apellido = form.cleaned_data['apellido']
            cliente.dni = form.cleaned_data['dni']
            cliente.telefono = form.cleaned_data['telefono']
            cliente.email = form.cleaned_data['email']
            cliente.direccion = form.cleaned_data['direccion']
            cliente.ciudad = form.cleaned_data['ciudad']
            cliente.cumpleaños = form.cleaned_data['cumpleaños']
            cliente.save()
            return redirect('clienteListar')
    else:
        initial_data = {
            'nombre': cliente.nombre,
            'apellido': cliente.apellido,
            'dni': cliente.dni,
            'telefono': cliente.telefono,
            'email': cliente.email,
            'direccion': cliente.direccion,
            'ciudad': cliente.ciudad,
            'cumpleaños': cliente.cumpleaños,
        }
        form = forms.ClienteAltaForm(initial=initial_data)
    return render(request, 'pasticceria/clienteActualizar.html', {'form': form})

# Borrar cliente
def clienteBorrar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clienteListar')
    return render(request, 'pasticceria/clienteBorrar.html', {'cliente':cliente})


## ------- PRODUCTOS ----------------------------------------------------------------------
# ____ productos Listar ____
class ProductoListView(ListView):
    model = Producto
    context_object_name = "productos"
    template_name = "pasticceria/productoListar.html"
    ordering = ["codigo"]

# def menu(request):
#     productos = Producto.objects.all()
#     return render(request, "pasticceria/menu.html", {"productos" : productos})

# def cafe(request):
#     cafeteria = {
#         "cafes": [
#             {"French Vanilla":3.00},
#             {"Caramel Macchiato":3.75},
#             {"Pumpkin Spice":3.50},
#             {"Hazelnut":4.00},
#             {"Mocha":4.50}
#             ]
#     }

#     return render(request, "pasticceria/cafe.html", cafeteria)

# ____ productos Alta ____
class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductosForm
    template_name = "pasticceria/productoAlta.html"
    success_url = reverse_lazy('productoListar')

# ____ productos Actualizar ____
class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductosForm
    template_name = "pasticceria/productoAlta.html"
    success_url = reverse_lazy('productoListar')

# ____ productos Borrar ____
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "pasticceria/productoBorrar.html"
    success_url = reverse_lazy('productoListar')


## ------- ORDEN ---------------------------------------------------------------  
# ____ orden crear ____  
def crear_orden(request):
    if request.method == 'POST':
        orden_form = OrdenForm(request.POST)
        if orden_form.is_valid():
            orden = orden_form.save()
            return redirect('anadir_orden_items', orden_id=orden.id)
    else:
        orden_form = OrdenForm()

    return render(request, 'pasticceria/crear_orden.html', {'orden_form': orden_form})

# ____ orden cancelar ____  
def ordenCancelar(request):
    pass

# ____ Añadir items a la orden ____ 
def anadir_orden_items(request, orden_id):
    orden = get_object_or_404(Orden, id=orden_id)
    if request.method == 'POST':
        orden_item_form = OrdenItemForm(request.POST)
        if orden_item_form.is_valid():
            orden_item = orden_item_form.save(commit=False)
            orden_item.orden = orden
            orden_item.save()
            return redirect('anadir_orden_items', orden_id=orden.id)  # Redirect to the same page to add more items
    else:
        orden_item_form = OrdenItemForm()

    orden_items = OrdenItem.objects.filter(orden=orden)

    return render(request, 'pasticceria/anadir_orden_items.html', {
        'orden_item_form': orden_item_form,
        'orden': orden,
        'orden_items': orden_items
    })

# ____ Editar item en orden ____ 
def ordenItemEditar(request, orden_id):
    pass

# ____ Borrar item de orden ____ 
def ordenItemBorrar(request, orden_id):
    pass


## ------- ADMIN ---------------------------------------------------------------  

def admin(request):
    my_context = {
        "mensaje": "Vista para admin"
    }

    return render(request, "pasticceria/admin.html", my_context)