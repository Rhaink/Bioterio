from django.db import models
from BioterioID.models import Animal

class AnimalBio(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name='ID Animal')
    marca = models.CharField(max_length=100)
    por_parto = models.BooleanField(default=False, verbose_name='Por Parto')
    por_cruce = models.BooleanField(default=False, verbose_name='Por Cruce')
    separacion = models.BooleanField(default=False)
    en_destete = models.BooleanField(default=False, verbose_name='En Destete')
    fecha_destete_bio= models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Destete')
    numero_crias_camada = models.IntegerField(blank=True, null=True, verbose_name='Número de Crías en Camada')

    def __str__(self):
        return self.animal.numero_identificacion

    class Meta:
        verbose_name = "Identificación Bitácora"
        verbose_name_plural = "Identificación Bitácora"

class RegistroDiario(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    fecha_registro= models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Registro')
    peso_gramos_registro = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Peso en gramos')
    medidas_cm_registro = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Medidas en cm')
    consumo_alimento_gramos_registro = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Alimentos en gramos')
    consumo_agua_ml_registro = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Agua en ml')

    def __str__(self):
        return f"{self.animal.numero_identificacion} - {self.fecha_registro}"
    
    class Meta:
        verbose_name = "Registro Diario"
        verbose_name_plural = "Registro Diario"

