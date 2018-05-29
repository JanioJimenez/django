from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    #path('usuario/', usuario, name = 'usuario'),
    path('registro', registro, name='registro'),
    path('usuario', gmail, name='gmail'),
    path('home', home, name='home'),
    path('editor', editor, name='editor'),
    path('estadistica', estadistica, name='estadistica'),
    path('perfil', perfil, name='perfil'),
    path('parser', parser, name='parser'),

]