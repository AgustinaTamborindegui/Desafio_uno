from django.urls import path
from . import views

# URS GLOBALES DEL MODULO DE APP FAMILIA, la cree yo, no vino con el resto de las carpetas
# por eso importe "django.urils" para poder trabajar con ellas 
# minuto 01:34:00 clase 18

urlpatterns = [
    path ("", views.inicio),
    path ("lista_familiares", views.lista_familiares),
    path ("alta_familiares", views.alta_familiares),
    
]