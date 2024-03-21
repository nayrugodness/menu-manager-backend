from rest_framework import viewsets
from .models import CategoriaPlatillo, Platillo
from .serializers import CategoriaPlatilloSerializer, PlatilloSerializer

class CategoriaPlatilloViewSet(viewsets.ModelViewSet):
    queryset = CategoriaPlatillo.objects.all()
    serializer_class = CategoriaPlatilloSerializer

class PlatilloViewSet(viewsets.ModelViewSet):
    queryset = Platillo.objects.all()
    serializer_class = PlatilloSerializer
