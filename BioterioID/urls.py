from django.urls import path
from . import views

urlpatterns = [
    path('animales/', views.lista_animales, name='lista_animales'),
]
