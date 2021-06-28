from django.urls import path

from . import views

urlpatterns = [
    ###############URLS de store###############
    
    path('', views.Pantalla_Principal, name="Home"),
    path('Acera_de', views.Acera_de, name="Acerca de"), 
    path('ResultadoBusqueda/',views.Resultado_de_Busqueda, name="Resultado de Busqueda"),
    path('PantallaProducto/',views.Pantalla_de_Producto, name="Pantalla de Producto"),
    path('PantallaCargaProducto/',views.Pantalla_de_Cargar_Producto, name="Pantalla de Cargar Producto"),
    path('Pantalla_de_Contacto/',views.Pantalla_de_Contacto, name="Pantalla de Contacto"),
    path('PantallaEditaBorrar/', views.Pantalla_de_Edita_Borrar, name="Pantalla de Editar o Borar Producto"),
    path('Pantalla_de_Carito/',views.Pantalla_de_Carito, name="Pantalla de Carrito"),
    path('Pantalla_de_Login/',views.Pantalla_de_Login, name="Pantalla de Login"),
    path('Pantalla_de_Registro/',views.Pantalla_de_Registro, name="Pantalla de Registro"),
    #####################################
]

