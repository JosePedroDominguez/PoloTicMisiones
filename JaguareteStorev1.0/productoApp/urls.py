from django.urls import path

from productoApp.views import Pantalla_de_Producto,Pantalla_de_Cargar_Producto,Pantalla_de_Edita_Borrar
urlpatterns = [
    ###############URLS de store###############
    path('PantallaProducto/',Pantalla_de_Producto, name="Pantalla de Producto"),
    path('PantallaEditaBorrar/', Pantalla_de_Edita_Borrar, name="Pantalla de Editar o Borar Producto"),
    path('PantallaCargaProducto/',Pantalla_de_Cargar_Producto.Producto, name="Pantalla de Cargar Producto"),
    path('formularioItem/',Pantalla_de_Cargar_Producto.Procesar_Producto, name="guardarItem"),
    #####################################
]
