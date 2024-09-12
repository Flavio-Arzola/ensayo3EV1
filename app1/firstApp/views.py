from django.shortcuts import render
from django.http import HttpResponse

def display(request):
    return HttpResponse('<h1 style="text-align: center; color: red">Hola mundo django prueba 2</h1>')

# Create your views here.
