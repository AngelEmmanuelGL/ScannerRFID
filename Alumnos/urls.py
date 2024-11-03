from django.urls import path
from . import views

urlpetterns = [
    path("addAlumnos/", views.addAlumno, name = "addAlumno"),
]
