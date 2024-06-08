from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .forms import OrdenForm, OrdenItemForm
from django.contrib import messages
from .models import Orden, OrdenItem


# Create your views here.
def index(request):
    my_context_var = {
        "userName": "Visitante",
        # 'dateTime': datetime.datetime.now()
    }

    return render(request, "pasticceria/index.html", my_context_var)


def client_list(request):

    my_context = {
        "names": ["Carlos Perez", "Patricia Fernandez", "Emanuel Manrique"],
        "payment_status": True,
    }

    return render(request, "pasticceria/client_list.html", my_context)


def abm_clients(request):

    context = {}

    # Empty form request
    if request == "GET":
        context["abm_clients_form"] = forms.AbmClientsForm()

    else:  # Asummig is a POST
        form = forms.AbmClientsForm(request.POST)
        context["abm_clients_form"] = form

        # Form validation
        if form.is_valid():
            # If correct, inform with message and redirect
            messages.success(request, "Cliente creado exitosamente")
            return redirect("index")

        # IF NO correct
        # else:
            
        #     messages.error(request, "Existe un error, revise los datos ingresados")

    return render(request, "pasticceria/abm_clients.html", {'form':form})

def menu(request):
    pasteleria = {
        "pasteles": [
            {"Donut":1.50},
            {"Cherry Pie":2.75},
            {"Cheesecake":3.00},
            {"Cinnamon Roll":2.50},
            ]
    }

    return render(request, "pasticceria/menu.html", pasteleria)

def cafe(request):
    cafeteria = {
        "cafes": [
            {"French Vanilla":3.00},
            {"Caramel Macchiato":3.75},
            {"Pumpkin Spice":3.50},
            {"Hazelnut":4.00},
            {"Mocha":4.50}
            ]
    }

    return render(request, "pasticceria/cafe.html", cafeteria)

def abmProductos(request):

    context = {}

    # Empty form request
    if request == "GET":
        context["abmProductos_form"] = forms.AbmProductosForm()

    else:  # Asummig is a POST
        form = forms.AbmProductosForm(request.POST)
        context["abmProductos_form"] = form

        # Form validation
        if form.is_valid():
            # If correct, inform with message and redirect
            messages.success(request, "Producto creado exitosamente")
            return redirect("index")

        # IF NO correct
        # Saty in form but showing an error

    return render(request, "pasticceria/abmProductos.html", {'form':form})

def crear_orden(request):
    if request.method == 'POST':
        orden_form = OrdenForm(request.POST)
        if orden_form.is_valid():
            orden = orden_form.save()
            return redirect('anadir_orden_items', orden_id=orden.id)
    else:
        orden_form = OrdenForm()

    return render(request, 'pasticceria/crear_orden.html', {'orden_form': orden_form})

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


def admin(request):
    my_context = {
        "mensaje": "Vista para admin"
    }

    return render(request, "pasticceria/admin.html", my_context)