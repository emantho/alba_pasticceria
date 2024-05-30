from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from . import forms
from .forms import AbmClientsForm
import datetime
from django.contrib import messages


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
            messages.success(request, "Client created successfully")
            return redirect("index")

        # IF NO correct
        # Saty in form but showing an error

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
            messages.success(request, "Client created successfully")
            return redirect("index")

        # IF NO correct
        # Saty in form but showing an error

    return render(request, "pasticceria/abmProductos.html", {'form':form})

def admin(request):
    my_context = {
        "mensaje": "Vista para admin"
    }

    return render(request, "pasticceria/admin.html", my_context)