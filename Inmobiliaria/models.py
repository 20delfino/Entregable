from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length = 40)
    correo = models.EmailField()
    telefono = models.IntegerField()
    
    def __str__(self):
        return self.nombre

class Propietario(models.Model):
    nombre = models.CharField(max_length = 40)
    correo = models.EmailField()
    telefono = models.IntegerField()
    propiedades = models.IntegerField()

    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    ubicacion = models.CharField(max_length = 100)
    precio = models.IntegerField()
    tamaño = models.IntegerField()
    estado = models.CharField(max_length = 30)
    #propietario = models.ForeignKey('Propietario', on_delete = models.CASCADE, default = None)
    def __str__(self):
        return self.ubicacion

class Casa(models.Model):
    ubicacion = models.CharField(max_length = 100)
    precio = models.IntegerField()
    tamaño = models.IntegerField()
    estado = models.CharField(max_length = 30)
    #propietario = models.ForeignKey('Propietario', on_delete = models.CASCADE, default = None)
    def __str__(self):
        return self.ubicacion