from django.shortcuts import render
from .models import *
# Create your views here.
def listarPedidos(request):
    pedidos=Pedido.objects.all()
    if request.method=='POST':
        for p in pedidos:
            if p.usuario.dni==2:
                return render(request,"index",{
                    'pedidos':pedidos
                })


