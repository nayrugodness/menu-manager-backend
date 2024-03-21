from django.db import models
import uuid

class CategoriaPlatillo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Platillo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    precio = models.IntegerField()
    imagen = models.CharField(max_length=255)
    descripcion = models.TextField()
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(CategoriaPlatillo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
