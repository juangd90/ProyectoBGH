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
          #trae ok el dni del formulario
          # falta hacer la logica y comparar para mostrar el resultado  
         return render(request,"app/resultados.html",{
                   "dni":dni    
                 })
            

     else:        
        return render(request,"app/busqueda.html")
        

#falta agregar el html para la consulta y el html donde muestra el resultado

