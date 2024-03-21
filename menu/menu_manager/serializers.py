from rest_framework import serializers
from .models import CategoriaPlatillo, Platillo

class CategoriaPlatilloSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaPlatillo
        fields = ('id', 'nombre')

class PlatilloSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)

    class Meta:
        model = Platillo
        fields = ('id', 'nombre', 'precio', 'imagen', 'descripcion', 'categoria', 'categoria_nombre')
