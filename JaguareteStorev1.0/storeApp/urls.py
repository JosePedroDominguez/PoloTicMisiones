from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    ###############URLS de store###############
    
    path('', views.Pantalla_Principal, name="Home"),
    path('Acera_de', views.Acera_de, name="Acerca de"), 
    path('Pantalla_de_Contacto/',views.Pantalla_de_Contacto, name="Pantalla de Contacto"),
    path('Pantalla_de_Carito/',views.Pantalla_de_Carito, name="Pantalla de Carrito"),
    path('tags/',views.tags, name="tags"),
    path('buscar/',views.buscar, name="buscar"),
    #####################################
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)