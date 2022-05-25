from rest_framework import viewsets
from backend.models.ventas import Ventas
from backend.serializers.VentasSerializers import VentasSerializers

class VentasCreateView(viewsets.ModelViewSet):
    queryset = Ventas.objects.all().order_by("id_venta")
    serializer_class = VentasSerializers 