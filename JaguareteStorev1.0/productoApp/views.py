from django.shortcuts import render

from django.http import HttpRequest

from productoApp.forms import FomularioItem

from productoApp.models import Items
# Create your views here.
def Pantalla_de_Producto(request):

    return  render(request,'PantallaProducto.html')


class Pantalla_de_Cargar_Producto (HttpRequest):#SOLO VISIBLE PARA LOS ADMINISTRADORES
    def Producto(request):
        item = FomularioItem()
        return(render(request,"CargaDeProducto.html", {"form": item}))
    def Procesar_Producto(request):
        item = FomularioItem(request.POST)
        if item.is_valid():
            item.save()
            item = FomularioItem()
        return (render(request,"CargaDeProducto.html",{"form": item, "mensaje":"OK"}))


def Pantalla_de_Edita_Borrar(request):#SOLO VISIBLE PARA LOS ADMINISTRADORES

    return  render(request,'EdicionOBoradoDeProducto.html')

def Resultado_de_Busqueda(request):
    items = Items.objects.all()
    return(render(request,"ResultadoBusqueda.html",{"items": items}))