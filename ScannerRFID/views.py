from django.shortcuts import render
from django.http import HttpResponse
from Alumnos.models import ALumnos
from Maestros.models import Mestros


#pruebas
def prueba(request):
    return render(request, "prueba.html", {})

def mostrar(request):
    allData = ALumnos.objects.all
    return render(request, "", {"data":allData})
#index
def index(request):
    return render(request, "index.html", {})
#create 
def alumno(request):
    name = "Angel Emmanuel"
    new_alumno = ALumnos.objects.create(
        name = name,
        last_name = "Garcia Leana",
        n_reticulate = 23680406,
        semester = 3,
        career = "Ingenieria en Sistemas",
        RFID = "0001481820",
    )
    new_alumno.save()
    return HttpResponse(f"Alumno con nombre {name} se ah dado de alta")
    py
def maestro(request):
    name = "gerardo"
    new_maestro = Mestros.objects.create(
        name = name,
        last_name = "Acevedo Vega",
        n_reticulate = 12680034,
        RFID = "0002323411",
    )
    new_maestro.save()
    return HttpResponse(f"Maestro con nombre {name} se ah dado de alta")
    
def consulta(request):
    rfid = request.GET["rfid"]
    try: 
        get_data = Mestros.objects.get(RFID = rfid)
    except Mestros.DoesNotExist:
        get_data = ALumnos.objects.get(RFID = rfid)