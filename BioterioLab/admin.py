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
        fila = [obj.animal.numero_identificacion, obj.animal.tipo_animal, obj.animal.observaciones]
        ws.append(fila)

    wb.save(response)
    return response

exportar_a_excel.short_description = "Exportar seleccionados a Excel"

class AnimalProduccionAdmin(admin.ModelAdmin):
    list_display = ('get_animal_numero_identificacion', 'get_animal_tipo_animal', 'tipo_nacimiento', 'get_animal_numero_parto')
    list_filter = ('animal__tipo_animal', 'tipo_nacimiento')
    search_fields = ('get_animal_numero_identificacion', 'get_animal_sepa')
    actions = [exportar_a_excel]
        
    def get_animal_numero_identificacion(self, obj):
        return obj.animal.numero_identificacion
    get_animal_numero_identificacion.short_description = 'Número de Identificación'

    def get_animal_tipo_animal(self, obj):
        return obj.animal.tipo_animal
    get_animal_tipo_animal.short_description = 'Tipo de Animal'

    def get_animal_numero_parto(self, obj):
        return obj.animal.numero_parto
    get_animal_numero_parto.short_description = 'Número de Parto'

    def get_animal_sepa(self, obj):
        return obj.animal.sepa
    get_animal_sepa.short_description = 'Sepa de Animal'

admin.site.register(AnimalProduccion, AnimalProduccionAdmin)

class AnimalInvestigacionAdmin(admin.ModelAdmin):
    list_display = ('get_animal_numero_identificacion', 'get_animal_tipo_animal', 'get_animal_fecha_nacimiento', 'fecha_destete')
    list_filter = ('animal__tipo_animal',)
    search_fields = ('get_animal_numero_identificacion', 'get_animal_sepa')
    actions = [exportar_a_excel]

    def get_animal_numero_identificacion(self, obj):
        return obj.animal.numero_identificacion
    get_animal_numero_identificacion.short_description = 'Número de Identificación'

    def get_animal_tipo_animal(self, obj):
        return obj.animal.tipo_animal
    get_animal_tipo_animal.short_description = 'Tipo de Animal'

    def get_animal_numero_parto(self, obj):
        return obj.animal.numero_parto
    get_animal_numero_parto.short_description = 'Número de Parto'

    def get_animal_sepa(self, obj):
        return obj.animal.sepa
    get_animal_sepa.short_description = 'Sepa de Animal'

    def get_animal_fecha_nacimiento(self, obj):
        return obj.animal.fecha_nacimiento
    get_animal_fecha_nacimiento.short_description = 'Fecha de nacimiento de Animal'

admin.site.register(AnimalInvestigacion, AnimalInvestigacionAdmin)

