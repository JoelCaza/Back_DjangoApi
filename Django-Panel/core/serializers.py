# core/serializers.py

from rest_framework import serializers
from .models import Estudiante, Asistencia, Horario

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'  # Incluir todos los campos del modelo Estudiante

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = '__all__'  # Incluir todos los campos del modelo Asistencia

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'  # Incluir todos los campos del modelo Horario
