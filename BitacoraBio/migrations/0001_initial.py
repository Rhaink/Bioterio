# Generated by Django 4.2.7 on 2023-11-20 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_identificacion', models.CharField(max_length=50, unique=True)),
                ('tipo_animal', models.CharField(choices=[('rata', 'Rata'), ('raton', 'Ratón'), ('cobayo', 'Cobayo'), ('conejo', 'Conejo'), ('ave', 'Ave'), ('gato', 'Gato')], max_length=6)),
                ('sepa', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('por_parto', models.BooleanField(default=False)),
                ('numero_parto', models.IntegerField(blank=True, null=True)),
                ('por_cruce', models.BooleanField(default=False)),
                ('separacion', models.BooleanField(default=False)),
                ('en_destete', models.BooleanField(default=False)),
                ('fecha_fin_destete', models.DateField(blank=True, null=True)),
                ('numero_crias_camada', models.IntegerField(blank=True, null=True)),
                ('observaciones', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroDiario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('peso_gramos', models.DecimalField(decimal_places=2, max_digits=6)),
                ('medidas_cm', models.DecimalField(decimal_places=2, max_digits=6)),
                ('consumo_alimento_gramos', models.DecimalField(decimal_places=2, max_digits=6)),
                ('consumo_agua_ml', models.DecimalField(decimal_places=2, max_digits=6)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BitacoraBio.animal')),
            ],
        ),
    ]
