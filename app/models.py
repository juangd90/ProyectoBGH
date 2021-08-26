from datetime import date
from django.db import models
from django.db.models.enums import Choices
from django.utils import timezone
# Create your models here.
marcas=(
    ("BGH","BGH"),
    ("Philips","Philips"),
    ("LG","LG"),
    ("Noblex","Noblex"),
    ("Atma","Atma"),
    ("Otro","Otro")
)
opciones=(
    ("Si","Si"),
    ("No","No")
)
estado=(
    ("En proceso","En proceso"),
    ("Finalizado","Finalizado"),
    ("Reparado","Reparado"),
    ("Listo para retirar","Listo para retirar")
)
class Usuario(models.Model):
    nombre=models.CharField(max_length=64)
    apellido=models.CharField(max_length=64)
    dni=models.IntegerField()
    celular=models.CharField(max_length=10)
    domicilio=models.CharField(max_length=64,default="")
    #pedidos=models.ManyToManyField(Pedido,blank=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Pedido(models.Model):
    fecha_ingreso=models.DateTimeField()    
    marca=models.CharField(max_length=64,choices=marcas,default="BGH")
    garantia=models.CharField(max_length=64,choices=opciones,default="Si")
    detalle=models.CharField(max_length=200)
    comentarios=models.CharField(max_length=200,blank=True)
    estado=models.CharField(max_length=64,choices=estado,default="En proceso",)
    monto=models.CharField(max_length=5,blank=True)
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    def __str__(self):
      return  f"Pedido #{self.id} con ingreso el {self.fecha_ingreso} del cliente {self.usuario}- DNI {self.usuario.dni}"


class pedidoNoUsuario(models.Model):
    nombre_y_apellido=models.CharField(max_length=64)
    celular=models.CharField(max_length=10)
    retiro_en_domicilio=models.CharField(max_length=2,choices=opciones,default="Si")
    domicilio=models.CharField(max_length=64,default="")
    barrio=models.CharField(max_length=64,default="")
    comentarios=models.TextField(max_length=300,default="")
    
    def __str__(self):
        return f"El cliente {self.nombre_y_apellido} cargó un pedido"





