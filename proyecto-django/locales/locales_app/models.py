from django.db import models


# Create your models here.
class Barrio(models.Model):
    nombre = models.CharField(max_length=200)
    siglas = models.CharField(max_length=10)


class Persona(models.Model):
    nombre = models.CharField(max_length=300)
    apellido = models.CharField(max_length=300)
    cedula = models.CharField(max_length=10)
    correo = models.EmailField()


class LocalesComida(models.Model):
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=300)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)
    comida_tipo = models.CharField(max_length=500, )
    ventas_proyectadas = models.IntegerField()
    permiso = models.FloatField()


class LocalesRepuestos(models.Model):
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE)
    direccion = models.CharField(verbose_name = "direccion", max_length=300)
    barrio = models.ForeignKey(Barrio, on_delete = models.CASCADE)
    valor_mecaderia = models.FloatField()
    comida_tipo = models.CharField(max_length= 50)
    ventas_proyectadas = models.CharField(verbose_name = "ventas_proyectadas",max_length=200)
    permiso = models.FloatField()
