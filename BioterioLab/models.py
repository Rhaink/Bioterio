from django.db import models
from BioterioID.models import Animal

class AnimalLab(models.Model):
    ESTADO_OPCIONES = [
        ('lactante', 'Lactante'),
        ('adulto', 'Adulto'),
        ('gestante', 'Gestante'),
    ]
        
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name='ID Animal')
    estado_animal = models.CharField(max_length=8, choices=ESTADO_OPCIONES, verbose_name='Estado del Animal', default='adulto')

    def __str__(self):
        return f"{self.animal.tipo_animal} - {self.animal.numero_identificacion}"
    
class AnimalProduccion(AnimalLab):
    NACIMIENTO_OPCIONES = [
        ('natural', 'Parto Natural'),
        ('in vitro', 'In Vitro'),
    ]
        
    fecha_produccion= models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Producción')
    peso_gramos_produccion = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Peso en gramos')
    medidas_cm_produccion = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Medidas en cm')
    consumo_alimento_gramos_produccion = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Alimentos en gramos')
    consumo_agua_ml_produccion = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Agua en ml')
    tipo_nacimiento = models.CharField(max_length=8, choices=NACIMIENTO_OPCIONES, verbose_name='Tipo de Nacimiento', default='natural')

    def __str__(self):
        return f"{self.animal.numero_identificacion} - {self.fecha_produccion}"

    class Meta:
        verbose_name = "Producción"
        verbose_name_plural = "Producción"

class AnimalInvestigacion(AnimalLab):
    fecha_destete= models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Destete')

    class Meta:
        verbose_name = "Investigación"
        verbose_name_plural = "Investigación"



