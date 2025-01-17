# core/models.py

from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Asistencia(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha = models.DateField()
    presente = models.BooleanField(default=False)

    def __str__(self):
        return f"Asistencia de {self.estudiante} en {self.fecha}"

class Horario(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    dia = models.CharField(max_length=10)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"Horario de {self.estudiante} en {self.dia} de {self.hora_inicio} a {self.hora_fin}"
