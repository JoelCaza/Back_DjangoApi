# core/urls.py

from django.urls import path
from .views import EstudianteList, EstudianteDetail, AsistenciaList, HorarioList

urlpatterns = [
    path('estudiantes/', EstudianteList.as_view(), name='estudiantes-list'),
    path('estudiantes/<int:pk>/', EstudianteDetail.as_view(), name='estudiante-detail'),
    path('asistencias/', AsistenciaList.as_view(), name='asistencia-list'),
    path('horarios/', HorarioList.as_view(), name='horario-list'),
]
