from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.prueba , name = "index"),
    path("Alumnos/", include("Alumnos.urls")),
    path('consultar_alumno/', views.consul, name='consultar_alumno'),
]