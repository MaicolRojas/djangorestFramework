from rest_framework import serializers
from backend.models.ventas import Ventas

from backend.models.clientes import Clientes
from backend.serializers.ClienteSerializers import ClienteSerializers

from backend.models.usuarios import Usuarios
from backend.serializers.UsuariosSerializers import UsuariosSerializers

from backend.models.productos import Productos
from backend.serializers.ProductosSerializers import ProductosSerializers

from backend.models.categoria import Categoria
from backend.serializers.CategoriaSerializers import Categoriaserializers

class VentasSerializers(serializers.ModelSerializer):
   Cliente = ClienteSerializers()
   Usuarios = UsuariosSerializers()
   Productos = ProductosSerializers()
   Categorias = Categoriaserializers()
   
   class Meta:
      model = Ventas
      fields = '__all__'
      
   def to_representation(self, obj):
      ventas = Ventas.objects.get(id_venta=obj.id_venta)
      clientes = Clientes.objects.get(ventas=obj.id_venta)
      usuarios = Usuarios.objects.get(ventas=obj.id_venta)
      productos = Productos.objects.get(ventas=obj.id_venta)
      categorias = Categoria.objects.get(productos=obj.id_producto)
      return{
         "id_venta":ventas.id_venta,
         "codigo": ventas.codigo,
         "productos": ventas.productos,
         "impuesto": format(ventas.impuesto , ",.0f"),
         "neto": format(ventas.neto, ",.0f"),
         "total": format(ventas.total, ",.0f"),
         "metodo_pago": ventas.metodo_pago,
         "fecha_venta": format(ventas.fecha_venta,'%Y-%m-%d %H:%M:%S'),
         "Cliente":{
            "id_cliente": clientes.id_cliente,
            "nombre": clientes.nombre,
            "documento": format(clientes.documento,",.0f"),
            "email": clientes.email,
            "telefono": clientes.telefono,
            "direccion": clientes.direccion,
            "fecha_nacimiento": clientes.fecha_nacimiento,
            "compras": clientes.compras,
            "Ultima_compra": format(clientes.Ultima_compra,'%Y-%m-%d %H:%M:%S')
         },
         "Usuario":{
            "id_usuario": usuarios.id_usuario,
            "nombre": usuarios.nombre,
            "username": usuarios.username,
            "perfil": usuarios.perfil,
            "foto": "https://sistema-control-inventario.herokuapp.com"+usuarios.foto.url,
            "estado": usuarios.estado,
            "ultimo_ingreso": format(usuarios.ultimo_ingreso,'%Y-%m-%d %H:%M:%S')
         },
         "Productos":{
            'id_producto': productos.id_productos,
            "codigo": productos.codigo,
            "producto" : productos.producto ,
            "imagen": "https://sistema-control-inventario.herokuapp.com"+productos.imagen.url,
            "stock": productos.stock,
            "precio_compra" : format(productos.precio_compra,",.0f"),
            "precio_venta": format(productos.precio_venta,",.0f"),
            "venta": productos.venta,
            "fecha": format(productos.fecha,'%Y-%m-%d %H:%M:%S'),
            "Categorias":{
                "id_categoria": categorias.id_categoria,
                "categoria": categorias.categoria,
                "fecha": format(categorias.fecha,'%Y-%m-%d %H:%M:%S')
            }
         },
      }