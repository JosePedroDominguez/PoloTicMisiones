from django.shortcuts import render,HttpResponse

from storeApp.models import Items
# Create your views here.

def Acera_de(request):

    return  render(request,"template/AcercaDe.html")
    
def Pantalla_Principal(request):

    return render(request,"template/Home.html")


def Pantalla_de_Contacto(request):
    return  render(request,"template/Contacto.html")

def Pantalla_de_Producto(request):

    return  render(request,"template/PantallaProducto.html")

def Pantalla_de_Cargar_Producto(request):#SOLO VISIBLE PARA LOS ADMINISTRADORES

    return  render(request,"template/CargaProducto.html")

def Pantalla_de_Edita_Borrar(request):#SOLO VISIBLE PARA LOS ADMINISTRADORES

    return  render(request,"template/EdicionOBoradoDeProducto.html")

def Pantalla_de_Carito(request):
    return  render(request,"template/Carrito.html")

def Pantalla_de_Login(request):

    return  render(request,"template/Login.html")

def Pantalla_de_Registro(request):

    return  render(request,"template/Registro.html")


def Resultado_de_Busqueda(request):
    if request.GET["itm"]:
        
        producto = request.GET["itm"]

        if len(producto)>20 :#esto evita que se ingrese una cadena muy larga
            mesage = "texto de busqueda demasiado largo"
        else:
            articulos = Items.objects.filter(name__icontains=producto)
            return render(request, "ResultadoBusqueda.html", {"articulos":articulos, "query":producto})
    else:
        mesage = "No se introdujo nada"
    return HttpResponse(mesage)
    