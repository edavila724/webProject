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
    def __str__(self):
        return self.cliente +" / " +str(self.fecha)
    
class producto(models.Model):    
    opciones = ('c', 'Cosmetica'),('a', 'Aseo'),('v', 'Veduras'),('l', 'Licores')
    nombre = models.CharField(max_length=100)
    precio = models.FloatField(default=0)
    stock = models.IntegerField(default=0)
    codBarra = models.CharField(max_length=20, primary_key=True)
    categoria =models.CharField(max_length=15, choices= opciones)    
    def __str__(self):
        return self.nombre    
    
class item(models.Model):
    carrito = models.ForeignKey(carritoCompras, on_delete= models.CASCADE) 
    producto = models.ForeignKey(producto, on_delete= models.CASCADE)
    cantidad = models.IntegerField(default=0)
    def __str__(self):
        return self.carrito__str__()
      
