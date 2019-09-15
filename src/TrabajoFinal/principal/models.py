from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    victorias = models.CharField(max_length=10)
    derrotas = models.CharField(max_length=10)
    porcentaje = models.CharField(max_length=10)
    diferencia = models.CharField(max_length=10)
    puntosFavor = models.CharField(max_length=10)
    puntosContra = models.CharField(max_length=10)
   
    def __str__(self):
        return self.nombre
    
class Noticia(models.Model):
    titular = models.CharField(max_length=200)
    fecha = models.CharField(max_length=50)
    referencia = models.CharField(max_length=50)
    urlPartido = models.URLField(max_length=200)
    urlEquipo = models.URLField(max_length=200)
    
    def __str__(self):
        return self.referencia
    
class Jornada(models.Model):
    numero = models.CharField(max_length=10)
    local =  models.CharField(max_length=50)
    visitante = models.CharField(max_length=50)
    puntosL = models.CharField(max_length=10, null=True, blank=True)
    puntosV = models.CharField(max_length=10, null=True, blank=True)
    hora = models.CharField(max_length=10, null=True, blank=True)
    
    def __str__(self):
        return self.numero
        