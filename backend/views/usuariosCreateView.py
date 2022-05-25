from rest_framework import serializers, viewsets
from backend.models.usuarios import Usuarios
from backend.serializers.UsuariosSerializers import UsuariosSerializers

class UsuariosCreateView(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all().order_by("id_usuario")
    serializer_class = UsuariosSerializers 