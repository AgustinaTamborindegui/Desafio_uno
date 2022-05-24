from django.shortcuts import render
from datetime import datetime
from app_familia.models import Familiares
from django.http import HttpResponse

def inicio (request):
    
    return render (request, "index.html")

# Traigo la data de la base de datos
def lista_familiares (request):
    familiares = Familiares.objects.all()
    datos = {"datos": familiares}
    
    return render (request, "lista_familiares.html", datos)
    

def alta_familiares (request):
    familiar= Familiares(nombre = "Agustina", fecha_de_nacimiento = "1999-11-21", edad= 20)
    familiar.save()
    familiar = Familiares(nombre = "Ailen", fecha_de_nacimiento = "2000-01-07", edad= 22)
    familiar.save()
    familiar = Familiares (nombre = "Susana", fecha_de_nacimiento = "1990-12-09", edad= 40)
    familiar.save()

    return HttpResponse ("todo ok")
