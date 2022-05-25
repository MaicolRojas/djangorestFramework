from django.db import models
from .clientes import Clientes
from .usuarios import Usuarios
from .productos import Productos
from .enum import Pago

class Ventas(models.Model):
    id_venta = models.BigAutoField(primary_key=True)
    codigo = models.IntegerField()
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    productos = models.CharField('productos', max_length = 500)
    impuesto = models.DecimalField(max_digits=10, decimal_places=2)
    neto = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length = 20, choices=Pago.choices(), default='EF')
    fecha_venta = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.codigo)