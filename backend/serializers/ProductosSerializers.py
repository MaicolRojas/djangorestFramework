from rest_framework import serializers

from backend.models.productos import Productos

from backend.models.categoria import Categoria
from backend.serializers.CategoriaSerializers import Categoriaserializers

class ProductosSerializers(serializers.ModelSerializer):
    #Categorias = Categoriaserializers()
    class Meta:
        model = Productos
        fields = "__all__"  