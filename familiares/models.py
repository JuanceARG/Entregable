from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    fec_nac = models.DateField()
    relacion = models.CharField(max_length=40)

class Familiares(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    fec_nac = models.DateField()
    relacion = models.CharField(max_length=40)
