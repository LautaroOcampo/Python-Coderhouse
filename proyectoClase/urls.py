"""proyectoClase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('vista/', views.vista),
    path('fecha/', views.fecha),
    path('calcular-fecha/<int:edad>', views.calcular_fecha),
    path('template/', views.mi_template),
    path('template/<str:nombre>', views.template_persona),
    path('ver-personas/', views.ver_personas),
    path('crear-personas/<str:nombre>', views.crear_personas),
    path('admin/', admin.site.urls),
]
