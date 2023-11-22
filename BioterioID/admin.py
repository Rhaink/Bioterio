from django.http import HttpResponse
from openpyxl import Workbook
from django.contrib import admin
from .models import Animal

def exportar_a_excel(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="animales.xlsx"'

    wb = Workbook()
    ws = wb.active
    ws.title = "Animales"

    # Encabezados
    columns = ['ID', 'Tipo', 'Fecha Nacimiento', 'Sexo', 'Raza', 'Especie', 'Estado Vida']
    ws.append(columns)

    # Datos
    for animal in queryset:
        ws.append([animal.numero_identificacion, animal.tipo_animal, animal.fecha_nacimiento,
                   animal.sexo, animal.raza, animal.especie, animal.estado_vida])

    wb.save(response)
    return response

exportar_a_excel.short_description = "Exportar a Excel"

# Registro con una clase de administración personalizada
# Si deseas personalizar cómo se muestra el modelo en la interfaz de administración,
# puedes crear una clase de administración.

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('numero_identificacion', 'tipo_animal', 'fecha_nacimiento', 'sexo', 'raza', 'especie', 'estado_vida')
    list_filter = ('tipo_animal', 'sexo', 'estado_vida')
    search_fields = ('numero_identificacion', 'raza', 'especie')
    actions = [exportar_a_excel]

# Después, registra el modelo junto con la clase de administración
admin.site.register(Animal, AnimalAdmin)
