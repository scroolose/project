#from pipes import Template
#from django.http import HttpResponse
import datetime
#from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido, nacimiento, dni):
        self.nombre=nombre
        self.apellido=apellido
        self.nacimiento=nacimiento
        self.dni=dni


def familiares(request):

    p1=Persona("Maricel", "Dominguez", "04/03/1986", "32.000.000")
    p2=Persona("Rolando", "Dominguez", "12/09/2021", "50.000.000")
    p3=Persona("Prudencia", "Dominguez", "12/09/2021", "50.000.001")


    return render(request, "miplantilla.html", {
        "nombre_persona1":p1.nombre, "apellido_persona1":p1.apellido, "nacimiento_persona1":p1.nacimiento, "dni_persona1":p1.dni,
        "nombre_persona2":p2.nombre, "apellido_persona2":p2.apellido, "nacimiento_persona2":p2.nacimiento, "dni_persona2":p2.dni,
        "nombre_persona3":p3.nombre, "apellido_persona3":p3.apellido, "nacimiento_persona3":p3.nacimiento, "dni_persona3":p3.dni
        })


#def despedida(request):
#    return HttpResponse("Gracias por visitar nuestra pagina")

#def damefecha(request):
#    fecha_actual = datetime.datetime.now()
#    documento = """<htlm>
#    <body>
#    <h2>
#    Fecha y hora actuales %s
#    </h2>
#    </body>
#    </htlm>""" % fecha_actual

#    return HttpResponse(documento)

