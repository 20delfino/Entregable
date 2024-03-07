from django.urls import path
from Inmobiliaria.views import *

urlpatterns = [
    path("",inicio),
    path('usuario/', usuario),
    path('propietario/', propietario),
    path('departamento/', departamento),
    path('casa/', casa),
    path('buscar_usuario/', buscar_usuario),
    path('resultado/', mostrar_usuario),
]