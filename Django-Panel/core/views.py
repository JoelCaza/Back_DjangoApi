# core/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Estudiante, Asistencia, Horario
from .serializers import EstudianteSerializer, AsistenciaSerializer, HorarioSerializer

class EstudianteList(APIView):
    def get(self, request):
        estudiantes = Estudiante.objects.all()
        serializer = EstudianteSerializer(estudiantes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EstudianteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EstudianteDetail(APIView):
    def get_object(self, pk):
        try:
            return Estudiante.objects.get(pk=pk)
        except Estudiante.DoesNotExist:
            return None

    def get(self, request, pk):
        estudiante = self.get_object(pk)
        if estudiante is None:
            return Response({"error": "Estudiante no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EstudianteSerializer(estudiante)
        return Response(serializer.data)

    def put(self, request, pk):
        estudiante = self.get_object(pk)
        if estudiante is None:
            return Response({"error": "Estudiante no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EstudianteSerializer(estudiante, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        estudiante = self.get_object(pk)
        if estudiante is None:
            return Response({"error": "Estudiante no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        estudiante.delete()
        return Response({"message": "Estudiante eliminado"}, status=status.HTTP_204_NO_CONTENT)


class AsistenciaList(APIView):
    def get(self, request):
        asistencia = Asistencia.objects.all()
        serializer = AsistenciaSerializer(asistencia, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AsistenciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HorarioList(APIView):
    def get(self, request):
        horarios = Horario.objects.all()
        serializer = HorarioSerializer(horarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HorarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
