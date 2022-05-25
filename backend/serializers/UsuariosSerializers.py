from rest_framework import serializers
from backend.models.usuarios import Usuarios


class UsuariosSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Usuarios
        fields = '__all__'
    def to_representation(self, obj):
        usuarios = Usuarios.objects.get(id_usuario=obj.id_usuario)
        return{
            "id_usuarios": usuarios.id_usuario,
            "nombre": usuarios.nombre,
            "username": usuarios.username,
            "password": usuarios.password,
            "perfil": usuarios.perfil,
            "foto": "https://sistema-control-inventario.herokuapp.com"+usuarios.foto.url,
            "estado": usuarios.estado,
            "ultimo_ingreso": format(usuarios.ultimo_ingreso,'%Y-%m-%d %H:%M:%S')
        }