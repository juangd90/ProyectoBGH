from django import http,forms
from django.db.models import fields
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from .models import *
from django.contrib.auth import login,logout,authenticate
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
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

def login_admin(request):
   if request.user.is_authenticated:
        return redirect('app/index.html')
   else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')#tiene que direccionar al panel para editar los pedidos
       context={}
       return render(request,'app/login.html',context)

class PedidosListado(LoginRequiredMixin,ListView):
    login_url='login'
    model=Pedido
    template_name='app/listado.html'

class CrearPedido(LoginRequiredMixin,CreateView):
    login_url='login'
    model=Pedido
    form=Pedido
    fields="__all__"#para que django liste todos los campos
    success_url= reverse_lazy('admin_pedidos')
    

class ActualizarPedido(LoginRequiredMixin,UpdateView):
    model=Pedido
    form=Pedido
    fields="__all__"
    template_name="app/editar.html"
    success_url= reverse_lazy('admin_pedidos')



class EliminarPedido(LoginRequiredMixin,DeleteView):
    model=Pedido
    form=Pedido
    fields="__all__"
    success_url= reverse_lazy('admin_pedidos')
   
class DetallePedido(LoginRequiredMixin,DetailView):
    model=Pedido
    template_name='app/detalle.html'   

def logout_admin(request):
    logout(request)
    messages.info(request,"Deslogueado de manera correcta")
    return redirect('index')

class CrearUsuario(LoginRequiredMixin,CreateView):
    model=Usuario
    form=Usuario
    fields="__all__"
    success_url= reverse_lazy('crear')
            









