from pyexpat import model
from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=10)
    edad = models.IntegerField(null=True)
    fecha_nacimiento = models.DateField(null=True)

# Create your models here.
