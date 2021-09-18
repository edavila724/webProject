from django.db import models
from django.db.models.base import Model

# Create your models here.
class CarritoCompras(models.Model):
    cliente = models.CharField(max_length=50)
    descuento = models.FloatField(default=0)
    cantMinima = models.IntegerField(default=0)
    fecha = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.cliente
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    codBarras = models.CharField(max_length=20, primary_key=True)
    opciones = (('a', 'Aseo'), ('c', 'Cosmetico'), ('l', "Licores"), ('f', "Frutas y Verduras"), ('g', "Granos"))
    categoria = models.CharField(max_length=20, choices= opciones)
    def __str__(self):
        return self.nombre
class ItemCarro(models.Model):
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    producto =models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    def __str__(self):
        return self.carrito.__str__()