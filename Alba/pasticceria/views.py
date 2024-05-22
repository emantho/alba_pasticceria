from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    my_context_var = {
        'userName':'Diana',
        'dateTime': datetime.datetime.now()
    }
    
    return render(request, 'pasticceria/index.html', my_context_var)

