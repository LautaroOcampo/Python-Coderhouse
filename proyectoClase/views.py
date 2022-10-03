
from datetime import datetime
from django.http import HttpResponse
from django.template import Context, Template, loader
import random

from home.models import Persona


def vista(request):
    return HttpResponse("<h1>que acelga</h1>")

def fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'la fecha actual es {fecha_actual}')

def calcular_fecha(request, edad):
    fecha = 2022 - edad
    return HttpResponse(f'naciste en el año {fecha}')

def mi_template(request):
    cargar_archivo = open(r'C:\Users\Admin\Desktop\CoderHouse\Python\Proyecto\templates\mi_template.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    
    contexto = Context({'lista': list(range(1,11)), 'random': random.randrange(1,11)})
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)

def template_persona(request, nombre):
    # cargar_archivo = open(r'C:\Users\Admin\Desktop\CoderHouse\Python\Proyecto\templates\tu_template.html', 'r')
    # template = Template(cargar_archivo.read())
    # cargar_archivo.close()
    
    # contexto = Context({'persona':nombre,'apellido':'Ocampo'})
    # template_renderizado = template.render(contexto)
    # return HttpResponse(template_renderizado)
    template = loader.get_template('tu_template.html')
    template_renderizado = template.render({'persona':nombre})
    return HttpResponse(template_renderizado)
    
def crear_personas(request, nombre):
    
    persona = Persona(nombre=nombre, edad=random.randrange(1,100), fecha_nacimiento=datetime.now())
    persona.save()
    
    template = loader.get_template('crear_personas.html')
    template_renderizado = template.render({'persona':persona})
    return HttpResponse(template_renderizado)    

def ver_personas(request):
    
    personas = Persona.objects.all()
    
    template = loader.get_template('ver_personas.html')
    template_renderizado = template.render({'personas':personas})
    return HttpResponse(template_renderizado)    
