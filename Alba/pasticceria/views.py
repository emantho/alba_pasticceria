from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from . import forms
import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    my_context_var = {
        'userName':'Paola',
        'dateTime': datetime.datetime.now()
    }
    
    return render(request, 'pasticceria/index.html', my_context_var)

def client_list(request):
    
    my_context = {
        'names' : [
            "Carlos Perez",
            "Patricia Fernandez",
            "Emanuel Manrique"
        ], 
        'payment_status': True
        
    }
    
    return render(request, 'pasticceria/client_list.html', my_context)

def abm_clients(request):
    
    # Controlling request flow 
    
    context = {}
    
    # Empty form request
    if request == 'GET':
        context['abm_clients_form'] = forms.AbmClientsForm()
    
    else: # Asummig is a POST
        form = forms.AbmClientsForm(request.POST)
        context['abm_clients_form'] = form
    
        # Form validation
        if form.is_valid():
        # If correct, inform with message and redirect
            messages.success(request, 'Client created successfully')
            return redirect('index')
            
        # IF NO correct 
        # Saty in form but showing an error
        
    return render(request, 'pasticceria/abm_clients.html', context)