from django.shortcuts import render
from Inmobiliaria.models import *
from Inmobiliaria.forms import *

# Create your views here.

def inicio(request):
    return render(request, 'Inmobiliaria/inicio.html')

def usuario(request):

    if request.method == "POST":
        formulario = UsuarioForm(request.POST)

        if formulario.is_valid():
            info_dict = formulario.cleaned_data 
            nuevo_usuario = Usuario(nombre= info_dict["nombre"],
                                    correo = info_dict["correo"],
                                    telefono = info_dict["telefono"])
            nuevo_usuario.save()
    else:
        formulario = UsuarioForm()
    return render(request, 'Inmobiliaria/usuario.html', {'form':formulario})

def propietario(request):

    if request.method == "POST":
        formulario = PropietarioForm(request.POST)

        if formulario.is_valid():
            info_dict = formulario.cleaned_data 
            nuevo_propietario = Propietario(nombre= info_dict["nombre"],
                                    correo = info_dict["correo"],
                                    telefono = info_dict["telefono"],
                                    propiedades = info_dict["propiedades"])
            nuevo_propietario.save()
    else:
        formulario = PropietarioForm()
    return render(request, 'Inmobiliaria/propietario.html', {'form':formulario})

def departamento(request):
    
    if request.method == "POST":
        formulario = DepartamentoForm(request.POST)

        if formulario.is_valid():
            info_dict = formulario.cleaned_data 
            nuevo_departamento = Departamento(ubicacion= info_dict["ubicacion"],
                                    tamaño = info_dict["tamaño"],
                                    precio = info_dict["precio"],
                                    estado = info_dict["estado"])
            nuevo_departamento.save()
    else:
        formulario = DepartamentoForm()
    return render(request, 'Inmobiliaria/departamento.html', {'form':formulario})


def casa(request):
    
    if request.method == "POST":
        formulario = CasaForm(request.POST)

        if formulario.is_valid():
            info_dict = formulario.cleaned_data 
            nueva_casa = Casa(ubicacion= info_dict["ubicacion"],
                                    tamaño = info_dict["tamaño"],
                                    precio = info_dict["precio"],
                                    estado = info_dict["estado"])
            nueva_casa.save()
    else:
        formulario = CasaForm()
    return render(request, 'Inmobiliaria/casa.html', {'form':formulario})

def buscar_usuario(request):

    return render(request, 'Inmobiliaria/buscar_usuario.html')

def mostrar_usuario(request):
     usuario = request.GET["user"] 
     resultado = Usuario.objects.filter(nombre__iexact= usuario) 
     return render(request, 'Inmobiliaria/resultado.html', {{"resultado":resultado}})