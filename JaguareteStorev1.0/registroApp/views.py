from django.shortcuts import render

from django.http import HttpRequest

from registroApp.forms import FomularioUser


# Create your views here.
class Pantalla_de_Registro(HttpRequest):
    def Registro(request):
        user = FomularioUser()
        return(render(request,"Registro.html", {"form": user}))
    def Procesar_Registro(request):
        user = FomularioUser(request.POST)
        if user.is_valid():
            user.save()
            user = FomularioUser()
        return (render(request,"Registro.html",{"form": user, "mensaje":"OK"}))
