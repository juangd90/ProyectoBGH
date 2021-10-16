from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Pedido,Usuario,pedidoNoUsuario
# Register your models here
class PedidoNoUsuarioAdmin(admin.ModelAdmin):
    list_display=("nombre_y_apellido","domicilio","celular","comentarios","retiro_en_domicilio")




admin.site.register(Pedido)
admin.site.register(Usuario)
admin.site.register(pedidoNoUsuario,PedidoNoUsuarioAdmin)
