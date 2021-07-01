from django.shortcuts import render,HttpResponse

from django.contrib import messages
# Create your views here.

def Acera_de(request):

    return  render(request,'AcercaDe.html')
    
def Pantalla_Principal(request):

    return render(request,'Home.html')


def Pantalla_de_Contacto(request):
    return  render(request,'Contacto.html')


def Pantalla_de_Carito(request):
    return  render(request,'Carrito.html')

def Pantalla_de_Login(request):

    return  render(request,'Login.html')

