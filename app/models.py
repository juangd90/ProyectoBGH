from datetime import date
from django.db import models
from django.utils import timezone
# Create your models here.
marcas=(
    ("BGH","BGH"),
    ("Philips","Philips"),
    ("LG","LG"),
    ("Noblex","Noblex"),
    ("Atma","Atma")
)
opciones=(
    ("Si","Si"),
    ("No","No")
)
class Usuario(models.Model):
    nombre=models.CharField(max_length=64)
    apellido=models.CharField(max_length=64)
    dni=models.IntegerField()
    #pedidos=models.ManyToManyField(Pedido,blank=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Pedido(models.Model):
    fecha_ingreso=models.DateTimeField()
    fecha_salida=models.DateTimeField(null=False,blank=True)
    marca=models.CharField(max_length=64,choices=marcas,default="BGH")
    garantia=models.CharField(max_length=64,choices=opciones,default="Si")
    detalle=models.CharField(max_length=200)
    monto=models.FloatField()
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    def __str__(self):
      return  f"Pedido #{self.id} con ingreso el {self.fecha_ingreso} del cliente {self.usuario}- DNI {self.usuario.dni}"
    




