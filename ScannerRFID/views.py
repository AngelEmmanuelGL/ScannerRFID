from django.shortcuts import render
from django.http import HttpResponse
from Alumnos.models import ALumnos
from Maestros.models import Mestros
from django.http import JsonResponse
from datetime import datetime

#pruebas
def prueba(request):
    return render(request, "hindex2.html", {})

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
    rfid = request.GET["RFID"]
    try: 
        get_data = Mestros.objects.get(RFID = rfid)
    except Mestros.DoesNotExist:
        get_data = ALumnos.objects.get(RFID = rfid)
        
def consul(request):
    # Obtener el valor de 'numero' que será usado como 'id'
    numero = request.GET.get("numero")
    print("Número recibido:", numero)  # Agrega esta línea para ver qué número se está recibiendo
    if not numero:
        return JsonResponse({"error": "Número no proporcionado"}, status=400)

    try:
        # Consultar el alumno con el 'numero' que corresponde a 'id'
        alumno = ALumnos.objects.get(n_reticulate=numero)  # Asegúrate de que 'n_reticulate' sea el nombre correcto del campo
        hour = datetime.now().strftime("%H:%M:%S")
        data = {
            "nombre": alumno.name,
            "hora": hour,
        }
        return JsonResponse(data)

    except ALumnos.DoesNotExist:
        return JsonResponse({"error": "Alumno no encontrado"}, status=404)
