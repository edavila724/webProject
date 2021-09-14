from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey

# Comunicacion con base de datos
# Ejemplo de carrito de compras
class carritoCompras(models.Model):
    cliente = models.CharField(max_length=100)
    descuento = models.FloatField(default=0)
    cantMinima = models.IntegerField(default=0)
    fecha = models.DateField(auto_now_add=True)
    
class producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField(default=0)
    stock = models.IntegerField(default=0)
    codBarra = models.CharField(max_length=20, primary_key=True)
    categoria =models.CharField(max_length=10)
    
class item(models.Model):
    carrito = models.ForeignKey(carritoCompras, on_delete= CASCADE) 
    producto = models,ForeignKey(producto, on_delete= CASCADE)
    cantidad = models,IntegerField(default=0)
    

