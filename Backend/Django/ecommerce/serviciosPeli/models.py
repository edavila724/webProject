from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

class categoria(models.Model):
    publico = models.CharField(max_length=100)
    numVistas = models.IntegerField(default=0)
    
def __str__(self):
    pass
    return self.publico
def numVistas (self):
    pass
    self.numVistas +=1
    self.save()
    
class genero(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(categoria, on_delete= models.CASCADE)
    numVistas = models.IntegerField(default=0)
    numLikes = models.IntegerField(default=0)
    
def __str__(self):
    pass
    return self.nombre

def numVistas (self):
    pass
    self.categoria.nuevaVista()
    self.numVistas +=1
    self.save()
    
def nuevoLike(self):
    pass
    self.numLikes +=1
    self.save()
    
def disLike(self):
    pass
    self.numLikes -=1
    self.save()
    

   


