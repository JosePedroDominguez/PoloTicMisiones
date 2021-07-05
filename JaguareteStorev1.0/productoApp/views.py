
from django.core import paginator

from django.http.response import Http404

from django.shortcuts import render,redirect, get_object_or_404

from productoApp.forms import FomularioItem

from productoApp.models import Items

from productoApp.models import Tag

from django.contrib import messages

from django.core.paginator import Paginator

from django.contrib.auth.decorators import  permission_required
# Create your views here.
def Pantalla_de_Producto(request,id):
    it=Items.objects.filter(id=id)
    data={
        'prod':it
    }
    return  render(request,'PantallaProducto.html',data)

@permission_required('productoApp.add_items')
def Pantalla_de_Cargar_Producto(request):#SOLO VISIBLE PARA LOS ADMINISTRADORES
    data ={
        'form': FomularioItem()
    }
    if request.method == 'POST':
        formulario =FomularioItem( data=request.POST, files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Cargado Correctamante")
        else: 
            data["form"] = formulario
    return (render(request, "CargaDeProducto.html", data))
@permission_required('productoApp.view_items')
def listarItems(request):#SOLO VISIBLE PARA LOS ADMINISTRADORES
    itms = Items.objects.all()
    page = request.GET.get('page',1)#paginacion

    try:
        paginator = Paginator(itms,5)
        itms = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': itms,
        'paginator':paginator
    }

    return  (render(request,"adminItems.html",data))
@permission_required('productoApp.change_items')
def Editar(request, id):#SOLO VISIBLE PARA LOS ADMINISTRADORES
    prod = get_object_or_404(Items, id=id)
    data={
        'form':FomularioItem(instance=prod)
    }
    if request.method == 'POST':
        formulario =FomularioItem( data=request.POST,instance=prod ,files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editado Correctamante")
            return(redirect(to="Pantalla de Listar Productos"))
        else: 
            data["form"] = formulario    
    return  render(request,"editItem.html",data)

@permission_required('productoApp.delete_items')
def Borrar(request,id):#SOLO VISIBLE PARA LOS ADMINISTRADORES
    prod = get_object_or_404(Items, id=id)
    prod.delete()
    messages.success(request, "Eliminado Correctamante")
    return(redirect(to="Pantalla de Listar Productos"))

def Resultado_de_Busqueda(request):
    itm = Items.objects.all()
    data = {
        'productos': itm
    }
    return(render(request,"Home.html",data ))

def categorias(request):
    cat = Tag.objects.all()
    data={
        'Tags': cat
    }
    return(render(request,"categorias.html", data ))

def categoriasfiltradas(request,id):
    itm = Items.objects.filter(tag=id)
    data = {
        'catf': itm
    }
    return(render(request,"categoriasfiltradas.html",data ))
