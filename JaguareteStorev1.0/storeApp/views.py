from django.shortcuts import render,HttpResponse

from storeApp.models import Items,User
from django.contrib import messages
# Create your views here.

def Acera_de(request):

    return  render(request,'AcercaDe.html')
    
def Pantalla_Principal(request):

    return render(request,'Home.html')


def Pantalla_de_Contacto(request):
    return  render(request,'Contacto.html')

def Pantalla_de_Producto(request):

    return  render(request,'PantallaProducto.html')

def Pantalla_de_Cargar_Producto(request):#SOLO VISIBLE PARA LOS ADMINISTRADORES

    return  render(request,'CargaProducto.html')

def Pantalla_de_Edita_Borrar(request):#SOLO VISIBLE PARA LOS ADMINISTRADORES

    return  render(request,'EdicionOBoradoDeProducto.html')

def Pantalla_de_Carito(request):
    return  render(request,'Carrito.html')

def Pantalla_de_Login(request):

    return  render(request,'Login.html')

def Pantalla_de_Registro(request):
    if request.method == 'POST':
       correo = request.POST.get('correo','')
       usuario = request.POST.get('usuario','')
       contra = request.POST.get('contra','')
       usr = User( email=correo , user = usuario, password = contra)
       usr.save()
       messages.success(request,"Usurio creado con exito")
       return  render(request,'Registro.html')
    else:
        return  render(request,'Registro.html')




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
    