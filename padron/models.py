from django.db import models
from django.contrib.auth.models import User



class Sucursal(models.Model):
    descripcion = models.CharField(max_length=200, default=1)
    estado = models.BooleanField(default=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


class Ciudad(models.Model):
    descripcion = models.CharField(max_length=200)
    estado = models.BooleanField(default=True)
class Mesa(models.Model):
    descripcion = models.CharField(max_length=200)
    estado = models.BooleanField(default=True)


class Orden(models.Model):
    descripcion = models.CharField(max_length=200)
    estado = models.BooleanField(default=True)

    

class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    cedula = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    estado = models.BooleanField(default=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    mesa = models.ForeignKey(Mesa, on_delete= models.CASCADE)
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)






class Padron(models.Model):
    mesa = models.CharField(max_length=200)
    orden = models.CharField(max_length=200)
    monto_desembolso = models.IntegerField()
    estado = models.BooleanField(default=True)
    se_acerco = models.BooleanField(default=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField()