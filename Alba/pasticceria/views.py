from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from . import forms
import datetime

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
    
    if request == 'GET':
        context['abm_users_form'] = forms.AbmClientsForm()
    
    else: # Asummig is a POST
        context['abm_users_form'] = forms.AbmClientsForm(request.POST)
    
        # Form validation
        # If correct, inform with message and redirect 

        # IF NO correct 
        # Saty in form but showing an error
        # return redirect('index')
        
    return render(request, 'pasticceria/abm_clients.html', context)