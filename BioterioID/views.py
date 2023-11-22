from django.shortcuts import render
from .models import Animal

def lista_animales(request):
    animales = Animal.objects.all()
    return render(request, 'BioterioID/lista_animales.html', {'animales': animales})
