from django.urls import path
from Inmobiliaria.views import *

urlpatterns = [
    path("",inicio, name="inicio"),
    path('usuario/', usuario, name="usuario"),
    path('propietario/', propietario, name= "propietario"),
    path('departamento/', departamento, name="departamento"),
    path('casa/', casa, name="casa"),
    path('buscar_usuario/', buscar_usuario, name= "buscar_usuario"),
    path('resultado/', resultado_busqueda, name="resultado_busqueda"),
]