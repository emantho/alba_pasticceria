from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import Orden, OrdenItem, Producto, Cliente
from . import forms
from .forms import OrdenForm, OrdenItemForm, ProductosForm
from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum, DecimalField, ExpressionWrapper
from django.db.models.functions import Cast

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
        else:            
            messages.error(request, "Existe un error, revise los datos ingresados")
            
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
            messages.error(request, "Existe un error, revise los datos ingresados")

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
def actualizar_total_cost(orden):
    total = (
        OrdenItem.objects.filter(orden=orden).aggregate(
            total=Sum(
                ExpressionWrapper(F("producto__precio") * F("cantidad"), output_field=DecimalField())
            )
        )["total"]
        or 0.00
    )
    orden.total_cost = total
    orden.save()


# ____ Añadir items a la orden ____
def anadir_orden_items(request, orden_id):
    orden = get_object_or_404(Orden, id=orden_id)
    if request.method == 'POST':
        orden_item_form = OrdenItemForm(request.POST)
        if orden_item_form.is_valid():
            orden_item = orden_item_form.save(commit=False)
            orden_item.orden = orden
            orden_item.save()
            actualizar_total_cost(orden)
            return redirect('anadir_orden_items', orden_id=orden.id)  # Redirect to the same page to add more items
    else:
        orden_item_form = OrdenItemForm()

    orden_items = OrdenItem.objects.filter(orden=orden)
    valoresTotales = [item.total for item in orden_items]
    total_cost = sum(valoresTotales)

    return render(request, 'pasticceria/anadir_orden_items.html', {
        'orden_item_form': orden_item_form,
        'orden': orden,
        'orden_items': orden_items,
        'valoresTotales': valoresTotales,
        'total_cost' : orden.total_cost
    })

# ____ Editar item en orden ____
def ordenItemEditar(request, orden_id, item_id):
    orden = get_object_or_404(Orden, id=orden_id)
    orden_item = get_object_or_404(OrdenItem, id=item_id, orden=orden)
    if request.method == 'POST':
        orden_item_form = OrdenItemForm(request.POST, instance=orden_item)
        if orden_item_form.is_valid():
            orden_item_form.save()
            actualizar_total_cost(orden)
            return redirect('anadir_orden_items', orden_id=orden.id)
    else:
        orden_item_form = OrdenItemForm(instance=orden_item)
    return render(request, 'pasticceria/ordenItemEditar.html', {
        'orden_item_form': orden_item_form,
        'orden': orden,
        'orden_item': orden_item
    })

# ____ Borrar item de orden ____
def ordenItemBorrar(request, orden_id, item_id):
    orden = get_object_or_404(Orden, id=orden_id)
    orden_item = get_object_or_404(OrdenItem, id=item_id, orden=orden)
    if request.method == 'POST':
        orden_item.delete()
        actualizar_total_cost(orden)
        return redirect('anadir_orden_items', orden_id=orden.id)
    return render(request, 'pasticceria/ordenItemBorrar.html', {
        'orden_item': orden_item,
        'orden': orden
    })


## ------- LOGIN / LOGOUT---------------------------------------------------------------

def home(request):
    return render(request, "pasticceria/index.html")

@login_required
def restricted(request):
    return render(request, 'restricted.html')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        messages.success(self.request, 'You have successfully logged in.')
        return super().form_valid(form)

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, 'You have successfully logged out.')
        return super().dispatch(request, *args, **kwargs)
