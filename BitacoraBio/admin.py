from django.http import HttpResponse
from openpyxl import Workbook
from .models import AnimalBio, RegistroDiario
from django.contrib import admin

def exportar_registros_a_excel(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="registros_bitacora.xlsx"'
    wb = Workbook()
    ws = wb.active
    ws.title = "Registros Diarios"

    # Encabezados
    encabezados = [
        'ID Animal', 'Fecha', 'Peso (g)', 'Medidas (cm)', 
        'Consumo Alimento (g)', 'Consumo Agua (ml)'
    ]
    ws.append(encabezados)

    # Datos
    for registro in queryset:
        fila = [
            registro.animal.numero_identificacion, registro.fecha_registro.replace(tzinfo=None), 
            registro.peso_gramos_registro, registro.medidas_cm_registro, 
            registro.consumo_alimento_gramos_registro, registro.consumo_agua_ml_registro
        ]
        ws.append(fila)

    wb.save(response)
    return response

exportar_registros_a_excel.short_description = "Exportar a Excel"

class RegistroDiarioAdmin(admin.ModelAdmin):
    list_display = ('animal', 'fecha_registro', 'peso_gramos_registro', 'medidas_cm_registro')
    actions = [exportar_registros_a_excel]

admin.site.register(AnimalBio)
admin.site.register(RegistroDiario, RegistroDiarioAdmin)
