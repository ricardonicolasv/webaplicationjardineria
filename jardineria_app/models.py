#models.py
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .tipos import *
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    rut=models.CharField(max_length=12, null=False)
    direccion=models.CharField(max_length=500, null=False)

class Producto (models.Model):
    codigo_producto=models.CharField(max_length=50,primary_key=True)
    nombre_producto=models.CharField(max_length=50, null=False)
    cantidad=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(250)])
    tipo=models.CharField(max_length=25, choices=TIPO_PRODUCTO)
    precio=models.IntegerField(validators=[MinValueValidator(1000),MaxValueValidator(10000000)])
    imagen=models.ImageField(upload_to='producto', null=True)
    def __str__(self):
        return f"{self.codigo_producto} - {self.nombre_producto} {self.cantidad} {self.tipo}"
    
class Pedido(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido de {self.usuario.username} - {self.producto.nombre_producto}"
