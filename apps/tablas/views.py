from django.shortcuts import render
from django import forms
from .models import *

# Create your views here.
def index(request):
    return render(request, 'base.html')


def registro(request):
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
      try:
        Usuario.objects.get(email=email)
      except:
        if pass1 != request.POST['pass2']:
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
          return render(request,'gmail.html')
    return render(request,'registro.html')


def gmail(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        contraseña = request.POST['pass1']
        try:
            usuario = Usuario.objects.get(
                email = email,
                pass1 = contraseña
            )
            print(usuario)
            context = {
              'user': usuario,
            }
            return render(request,'home.html', context)
        except:
          pass
    return render(request, 'gmail.html')

def home(request):
    return render(request, 'home.html')

from ..parser.parser import evaluar
def editor(request):
  if request.method == 'POST':
    code = request.POST['code']
    resul = evaluar(str(request.POST['code']))
    context = {
      'code': code,
      'resul': resul,
    }
    return render(request, 'editor.html', context)
  return render(request, 'editor.html')

def estadistica(request):
    return render(request, 'estadistica.html')

def perfil(request):
    return render(request, 'perfil.html')

def parser(request):
  if request.method == 'POST':
    print(evaluar(str(request.POST['code'])))
  return render(request, 'perfil.html')