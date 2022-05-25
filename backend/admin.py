from django.contrib import admin

# Register your models here.

from .models.categoria import Categoria
from .models.productos import  Productos
from .models.clientes import  Clientes
from .models.usuarios import Usuarios
from .models.ventas import Ventas

admin.site.register(Categoria)
admin.site.register(Productos)
admin.site.register(Clientes)
admin.site.register(Usuarios)
admin.site.register(Ventas)

