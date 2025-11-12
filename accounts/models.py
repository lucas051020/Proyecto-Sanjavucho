from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.CharField(max_length=20, blank=True, null=True, verbose_name='DNI')
    telefono = models.CharField(max_length=50, blank=True, null=True, verbose_name='Teléfono')
    direccion = models.CharField(max_length=255, blank=True, null=True, verbose_name='Dirección')
    barrio = models.CharField(max_length=100, blank=True, null=True)
    codigo_postal = models.CharField(max_length=20, blank=True, null=True, verbose_name='Código Postal')
    provincia = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'Perfil de {self.usuario.username}'