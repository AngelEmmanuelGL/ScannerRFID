from django.shortcuts import render
from django.http import HttpResponse
from .models import ALumnos

def form_alumno(request):
    return render(request, "forms/Alumnos/Alumnos_form.html", {})

def mostrar(request):
    allData = ALumnos.objects.all()
    try:
        return render(request, "forms/Alumnos/MostStudentDetails.html", {"data":allData})
    except:
        return HttpResponse("archivo no encontrado")
    
def addAlumno(request):
    name = request.GET['name']
    last_name = request.GET['last_name']
    n_reticulate = request.GET['n_reticulate']
    semester = request.GET['semester']
    career = request.GET['career']
    RFID = request.GET['RFID']
    
    createAlumno = ALumnos.objects.create(name = name,
                                          last_name = last_name,
                                          n_reticulate = n_reticulate,
                                          semester = semester,
                                          career = career,
                                          RFID = RFID)
    return HttpResponse(f"Alumno con nombre: {createAlumno.name} creado")
