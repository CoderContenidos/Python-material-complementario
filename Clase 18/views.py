from django.shortcuts import render
from django.http import HttpResponse
from AppFamilia.models import Familiar
from django.template import loader
import datetime

# Create your views here.

def familiares(self):

    familiar1 = Familiar(nombre="Josué", edad=37, cumpleaños=datetime.date(1985, 5, 27))
    familiar2 = Familiar(nombre="Gabriel", edad=36, cumpleaños=datetime.date(1986, 10, 9))
    familiar3 = Familiar(nombre="Michelle", edad=34, cumpleaños=datetime.date(1988, 2, 28))
    familiar1.save()
    familiar2.save()
    familiar3.save()

    diccionario = {"pariente1":familiar1, "pariente2":familiar2, "pariente3":familiar3}

    plantilla = loader.get_template("familia/listaFamilia.html")

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)