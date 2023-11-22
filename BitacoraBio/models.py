from django.db import models

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
    marca = models.CharField(max_length=100)
    por_parto = models.BooleanField(default=False)
    numero_parto = models.IntegerField(blank=True, null=True)
    por_cruce = models.BooleanField(default=False)
    separacion = models.BooleanField(default=False)
    en_destete = models.BooleanField(default=False)
    fecha_fin_destete = models.DateField(blank=True, null=True)
    numero_crias_camada = models.IntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return self.numero_identificacion

class RegistroDiario(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    fecha = models.DateField()
    peso_gramos = models.DecimalField(max_digits=6, decimal_places=2)
    medidas_cm = models.DecimalField(max_digits=6, decimal_places=2)
    consumo_alimento_gramos = models.DecimalField(max_digits=6, decimal_places=2)
    consumo_agua_ml = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.animal.numero_identificacion} - {self.fecha}"

