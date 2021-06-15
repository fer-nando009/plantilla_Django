from django.http import HttpResponse
from datetime import datetime as dt

def saludo(request): #Primera vista
    return HttpResponse("Hola mundo, función de saludos de Django")

def despedida(request):
    return HttpResponse("Hasta pronto, vuelve cuando gustes")

def datetime(request):
    hora_fecha = dt.now()

    formato_fecha="""
    <html>
    <body>
    <h4>
    La hora acual es {}.
    </h4>
    </body>
    </html>""".format(hora_fecha)
    return HttpResponse(formato_fecha)
