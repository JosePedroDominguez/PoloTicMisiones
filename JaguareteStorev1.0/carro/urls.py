from django.urls import path

from . import views

app_name="carro"

urlpatterns = [
    ###############URLS de store###############
    path("agregar/<int:id>/", views.agregar_producto, name="agregar"),
    path("eliminar/<int:producto_id>/", views.eliminar_producto, name="eliminar"),
    path("restar/<int:producto_id>/", views.restar_producto, name="restar"),
    path("limpiar_carro/", views.limpiar_carro, name="limpiar_carro"),     
    #####################################
]



