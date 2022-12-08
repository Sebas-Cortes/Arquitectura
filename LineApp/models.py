from django.db import models
from django_userforeignkey.models.fields import UserForeignKey
from django.contrib.auth.models import User

# Create your models here.

class Estacionamiento(models.Model):
    idEstacionamiento = models.AutoField(primary_key=True, verbose_name='Id estacionamiendo')
    direccion = models.CharField(max_length=150, blank=False, null=False, verbose_name='Direccion')
    numero = models.IntegerField(blank=False, null=False, verbose_name='Numero de estacionamiendos disponibles')
    titular = UserForeignKey(auto_user_add=True, verbose_name='titular')

    def __str__(self):
        return self.direccion

class Arriendo(models.Model):
    idArriendo = models.AutoField(primary_key=True, verbose_name='id arriendo')
    arrendatario = UserForeignKey(auto_user_add=True, verbose_name='arrendatario')
    estacionamiento = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE)
    titular = models.IntegerField(blank=False, null=False, verbose_name='Id del titular')

    def __str__(self):
        return self.arrendatario