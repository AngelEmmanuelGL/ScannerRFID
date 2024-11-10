from django.urls import path
from . import views

urlpatterns = [
    path("addAlumnos/", views.addAlumno, name = "addAlumno"),
    path("form/", views.form_alumno, name = "form_alumno"),
    path("Most/", views.mostrar, name = "most")
]
