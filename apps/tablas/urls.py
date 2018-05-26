from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    #path('usuario/', usuario, name = 'usuario'),
    path('registro/', registro, name='registro'),
    path('usuario/', gmail, name='gmail'),
    path('home', home, name='home')
]