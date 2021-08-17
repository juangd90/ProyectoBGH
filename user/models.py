from django.db import models

# Create your models here.
class User(models.Model):
    nombre=models.CharField(max_length=64)
    apellido=models.CharField(max_length=64)
    dni=models.IntegerField()
    celular=models.CharField(max_length=10)
    #pedidos=models.ManyToManyField(Pedido,blank=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"