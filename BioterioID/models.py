from django.db import models

class Animal(models.Model):
    SEXO_OPCIONES = [
        ('macho', 'Macho'),
        ('hembra', 'Hembra'),
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

    numero_identificacion = models.CharField(max_length=4, unique=True,verbose_name='Número de Identificación')
    tipo_animal = models.CharField(max_length=6, choices=TIPO_ANIMAL_OPCIONES, verbose_name='Tipo de Animal',default='rata')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    sexo = models.CharField(max_length=6, choices=SEXO_OPCIONES, default='macho')
    sepa = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    inicio_produccion = models.DateField(verbose_name='Inicio de Producción')
    peso_gramos = models.IntegerField(verbose_name='Peso en gramos')
    longitud_cm = models.IntegerField(verbose_name='Longitud en cm')
    numero_parto = models.IntegerField(verbose_name='Número de Parto')
    estado_vida = models.CharField(max_length=6, choices=ESTADO_VIDA_OPCIONES, verbose_name='Estado de Vida', default='vivo')
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"{self.tipo_animal} - {self.numero_identificacion}"

    class Meta:
        verbose_name = "Identificación"
        verbose_name_plural = "Identificación"
