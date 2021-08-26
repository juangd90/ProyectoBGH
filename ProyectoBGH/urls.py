"""ProyectoBGH URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from app import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('pedidos',views.listarPedidos,name="pedidos"),
    path('login/',views.login_admin,name="login"),
    path('logout',views.logout_admin,name="logout"),
    path('admin_pedidos/',views.PedidosListado.as_view(template_name='app/listado.html'),name="admin_pedidos"),
    path('crear_usuario',views.CrearUsuario.as_view(template_name='app/crear_usuario.html'),name="crear_usuario"),
    path('admin_crear/',views.CrearPedido.as_view(template_name="app/crear.html"),name="crear"),
    path('admin_pedidos/eliminar/<int:pk>',views.EliminarPedido.as_view(),name="eliminar"),
    path('admin_pedidos/editar/<int:pk>',views.ActualizarPedido.as_view(),name="editar"),
    path('admin_pedidos/detalle/<int:pk>',views.DetallePedido.as_view(),name="detalle"),
    path('crear_pedido',views.PedidoNoUsuario.as_view(template_name="app/pedido.html"),name="crear_pedido"),

    
]
