from django import http
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request,"app/index.html")


def listarPedidos(request):
     if request.method=='POST':            
         dni=request.POST.get('dni')
         pedido_list=Pedido.objects.filter(usuario__dni=dni)
         #filtro de los pedidos todos los que coinciden con el dni ingresado        

          #trae ok el dni del formulario
          # falta hacer la logica y comparar para mostrar el resultado  
         return render(request,"app/resultados.html",{
                   "pedido_list":pedido_list    
                 })
        #se puede crear un objeto de tipo pedido para ir agregando ahi todos los resultados
        # al final se mostraria solamente ese objeto con un for en el html            

     else:        
        return render(request,"app/busqueda.html")
        



