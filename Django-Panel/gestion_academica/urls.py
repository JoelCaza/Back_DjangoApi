# gestion_academica/urls.py

from django.contrib import admin
from django.urls import path, include
from core import views  # Asegúrate de importar las vistas de core

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel de administración
    path('core/', include('core.urls')),  # Rutas para la aplicación core
      # Ruta para la página de inicio (URL raíz)
]
