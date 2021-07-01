from django.urls import path

from registroApp.views import Pantalla_de_Registro
urlpatterns = [
    ###############URLS de store###############
    
    #path('Pantalla_de_Login/',views.Pantalla_de_Login, name="Pantalla de Login"),
    path('Pantalla_de_Registro/',Pantalla_de_Registro.Registro, name="Pantalla de Registro"),
    path('fomulario/',Pantalla_de_Registro.Procesar_Registro, name="guardarUser"),
    #####################################
]

