from django.db import models

# Create your models here.
class Usuario(models.Model):
    primer_nombre = models.CharField(max_length=25)
    segundo_nombre = models.CharField(max_length=25)
    primer_apellido = models.CharField(max_length=25)
    segundo_apellido = models.CharField(max_length=25)
    email = models.EmailField()
    pass1 = models.CharField(max_length=25)
    edad = models.IntegerField()
    ciudad = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)
    lenguaje = models.CharField(max_length=50)

    def __str__(self):
        return "{} {} {} {}".format(self.primer_nombre,self.segundo_nombre,self.primer_apellido,self.segundo_apellido)

class Tipo_Lenguaje(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

class Lenguaje(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    tipo = models.ForeignKey(Tipo_Lenguaje, blank=True, null=True, on_delete=models.CASCADE)

class Ejecucion(models.Model):
    usuario = models.ForeignKey(Usuario, blank=True, null=True, on_delete=models.CASCADE)
    lenguaje = models.ForeignKey(Lenguaje, blank=True, null=True, on_delete=models.CASCADE)

class Codigo(models.Model):
    fecha = models.DateField()
    codigo = models.TextField(null=True, blank=True)
    ejecucion = models.OneToOneField(Ejecucion,on_delete=models.CASCADE)


