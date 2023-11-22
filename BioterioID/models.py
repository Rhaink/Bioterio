from django.db import models

class Animal(models.Model):
    SEXO_OPCIONES = [
        ('M', 'Macho'),
        ('H', 'Hembra'),
    ]
    TIPO_ANIMAL_OPCIONES = [
        ('rata', 'Rata'),
        ('raton', 'Ratón'),
        ('cobayo', 'Cobayo'),
        ('conejo', 'Conejo'),
        ('ave', 'Ave'),
        ('gato', 'Gato'),
    ]
    ESTADO_VIDA_OPCIONES = [
        ('vivo', 'Vivo'),
        ('muerto', 'Muerto'),
    ]

    numero_identificacion = models.CharField(max_length=50, unique=True)
    tipo_animal = models.CharField(max_length=6, choices=TIPO_ANIMAL_OPCIONES)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_OPCIONES)
    sepa = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    inicio_produccion = models.DateField()
    peso_gramos = models.IntegerField()
    longitud_cm = models.IntegerField()
    numero_parto = models.IntegerField()
    estado_vida = models.CharField(max_length=6, choices=ESTADO_VIDA_OPCIONES)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"{self.tipo_animal} - {self.numero_identificacion}"
