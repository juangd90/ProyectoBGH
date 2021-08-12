from django.contrib import admin
from .models import Pedido,Usuario
# Register your models here
class CategoryAdmin(admin.ModelAdmin):
    list_display=("name",)

class QuestionAdmin(admin.ModelAdmin):
    list_display=("texto_pregunta","categoria")

admin.site.register(Pedido)
admin.site.register(Usuario)