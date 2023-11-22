from django.http import HttpResponse
from openpyxl import Workbook
from django.contrib import admin
from .models import AnimalProduccion, AnimalInvestigacion

def exportar_a_excel(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="datos.xlsx"'
    wb = Workbook()
    ws = wb.active

    # Añade tus encabezados y datos aquí. Ejemplo para AnimalProduccion:
    encabezados = ['ID', 'Tipo de Animal', 'Número de Parto', 'Observaciones']
    ws.append(encabezados)

    for obj in queryset:
        fila = [obj.numero_identificacion, obj.tipo_animal, obj.observaciones]
        ws.append(fila)

    wb.save(response)
    return response

exportar_a_excel.short_description = "Exportar seleccionados a Excel"

class AnimalProduccionAdmin(admin.ModelAdmin):
    list_display = ('numero_identificacion', 'tipo_animal', 'es_por_parto', 'numero_parto')
    list_filter = ('tipo_animal', 'es_por_parto')
    search_fields = ('numero_identificacion', 'sepa')
    actions = [exportar_a_excel]

admin.site.register(AnimalProduccion, AnimalProduccionAdmin)

class AnimalInvestigacionAdmin(admin.ModelAdmin):
    list_display = ('numero_identificacion', 'tipo_animal', 'fecha_nacimiento', 'fecha_destete')
    list_filter = ('tipo_animal',)
    search_fields = ('numero_identificacion', 'sepa')
    actions = [exportar_a_excel]

admin.site.register(AnimalInvestigacion, AnimalInvestigacionAdmin)

