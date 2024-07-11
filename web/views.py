
from django.shortcuts import render # se agregó para llamar las paginas web del template

def index(request):
    return render(request, 'index.html')  

def about(request):
    return render(request, 'about.html')

def welcome(request):
    return render(request, 'welcome.html')