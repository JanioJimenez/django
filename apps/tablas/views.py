from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    context = {
        "mensaje":"holaaa",
    }
    return render(request, 'base.html', context)


def registro(request):
    context = {"mensaje":"hola"}

    if request.method == 'POST':
       nombres = request.POST['nombres']
       segnomb = request.POST['segnomb']
       priape = request.POST['priape']
       segape = request.POST['segape']
       edad = request.POST['edad']
       email = request.POST['email']       
       pais = request.POST['pais']
       ciudad = request.POST['ciudad']
       lenguaje = request.POST['lenguaje']
       pass1 = request.POST['pass1']

       usuario = Usuario.objects.create(
               primer_nombre = nombres,
               segundo_nombre = segnomb,
               primer_apellido = priape,
               segundo_apellido = segape,
               edad = edad,
               ciudad = ciudad,
               pais = pais,
               lenguaje = lenguaje,
               email = email,
               pass1 = pass1,
           )
       usuario.save()
       print("Exito")
    else:
        pass
    return render(request,'registro.html',context)


def gmail(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        contraseña = request.POST['pass1']
        try:
            usuario = Usuario.objects.get(
                email = email,
                pass1 = contraseña
            )
            return render(request,'home.html')
        except:
            pass
    return render(request, 'gmail.html')

def home(request):
    return render(request, 'home.html')

def editor(request):
    return render(request, 'editor.html')

def estadistica(request):
    return render(request, 'estadistica.html')

def perfil(request):
    return render(request, 'perfil.html')
