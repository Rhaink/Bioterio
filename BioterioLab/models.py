from django.db import models
from django.contrib.auth.models import User

class Animal(models.Model):
    TIPO_ANIMAL_OPCIONES = [
        ('rata', 'Rata'),
        ('raton', 'Ratón'),
        ('cobayo', 'Cobayo'),
        ('conejo', 'Conejo'),
        ('ave', 'Ave'),
        ('gato', 'Gato'),
    ]
    
    numero_identificacion = models.CharField(max_length=50, unique=True)
    tipo_animal = models.CharField(max_length=6, choices=TIPO_ANIMAL_OPCIONES)
    sepa = models.CharField(max_length=100)
    es_lactante = models.BooleanField(default=False)
    es_adulto = models.BooleanField(default=False)
    es_gestante = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True)
    usuarios_acceso = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f"{self.tipo_animal} - {self.numero_identificacion}"
    
class AnimalProduccion(Animal):
    historial_pesos = models.TextField(blank=True)
    historial_consumo_alimento = models.TextField(blank=True)
    historial_consumo_agua = models.TextField(blank=True)
    es_por_parto = models.BooleanField(default=False)
    numero_parto = models.PositiveIntegerField(blank=True, null=True)

class AnimalInvestigacion(Animal):
    fecha_nacimiento = models.DateField()
    fecha_destete = models.DateField(blank=True, null=True)


