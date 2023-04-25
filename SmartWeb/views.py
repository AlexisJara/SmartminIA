from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'paginas/index.html')

def iniciosesion(request):
    return render(request,'paginas/iniciosesion.html')

def registro(request):
    return render(request,'paginas/registro.html')