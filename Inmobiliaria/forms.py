from django import forms

# Create your forms here.

class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length = 40)
    correo = forms.EmailField()
    telefono = forms.IntegerField()

class PropietarioForm(forms.Form):
    nombre = forms.CharField(max_length = 40)
    correo = forms.EmailField()
    telefono = forms.IntegerField()
    propiedades = forms.IntegerField()

class DepartamentoForm(forms.Form):
    ubicacion = forms.CharField(max_length = 100)
    precio = forms.IntegerField()
    tamaño = forms.IntegerField()
    estado = forms.CharField(max_length = 30)
    #propietario = forms.ForeignKey('Propietario', on_delete = forms.CASCADE, default = None)

class CasaForm(forms.Form):
    ubicacion = forms.CharField(max_length = 100)
    precio = forms.IntegerField()
    tamaño = forms.IntegerField()
    estado = forms.CharField(max_length = 30)
    #propietario = forms.ForeignKey('Propietario', on_delete = forms.CASCADE, default = None)