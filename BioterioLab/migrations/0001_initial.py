# Generated by Django 4.2.7 on 2023-11-20 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_identificacion', models.CharField(max_length=50, unique=True)),
                ('tipo_animal', models.CharField(choices=[('rata', 'Rata'), ('raton', 'Ratón'), ('cobayo', 'Cobayo'), ('conejo', 'Conejo'), ('ave', 'Ave'), ('gato', 'Gato')], max_length=6)),
                ('sepa', models.CharField(max_length=100)),
                ('es_lactante', models.BooleanField(default=False)),
                ('es_adulto', models.BooleanField(default=False)),
                ('es_gestante', models.BooleanField(default=False)),
                ('observaciones', models.TextField(blank=True)),
                ('usuarios_acceso', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnimalInvestigacion',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='BioterioLab.animal')),
                ('fecha_nacimiento', models.DateField()),
                ('fecha_destete', models.DateField(blank=True, null=True)),
            ],
            bases=('BioterioLab.animal',),
        ),
        migrations.CreateModel(
            name='AnimalProduccion',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='BioterioLab.animal')),
                ('historial_pesos', models.TextField(blank=True)),
                ('historial_consumo_alimento', models.TextField(blank=True)),
                ('historial_consumo_agua', models.TextField(blank=True)),
                ('es_por_parto', models.BooleanField(default=False)),
                ('numero_parto', models.PositiveIntegerField(blank=True, null=True)),
            ],
            bases=('BioterioLab.animal',),
        ),
    ]
