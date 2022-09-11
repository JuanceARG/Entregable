# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from familiares.models import Familiares



def inicio(request):
    return render(request, "inicio.html")


def datosFam(self):
   
    miFlia = Familiares.objects.all()
    data={'miFlia':miFlia}    
    planilla = loader.get_template('datfamiliares.html')
    documento = planilla.render(data)
    return HttpResponse(documento)
    

