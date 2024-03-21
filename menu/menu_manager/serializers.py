from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaPlatilloViewSet, PlatilloViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaPlatilloViewSet)
router.register(r'platillos', PlatilloViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
