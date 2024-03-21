from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaPlatilloViewSet, PlatilloViewSet

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register('categorias', CategoriaPlatilloViewSet)
router.register('platillos', PlatilloViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('api/', include(router.urls)),
]
