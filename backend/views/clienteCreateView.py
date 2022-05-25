from rest_framework import viewsets
from backend.models.clientes import Clientes
from backend.serializers.ClienteSerializers import ClienteSerializers

class ClienteCreateView(viewsets.ModelViewSet):
    queryset = Clientes.objects.all().order_by("id_cliente")
    serializer_class = ClienteSerializers