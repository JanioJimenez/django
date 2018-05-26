from django.contrib import admin

from .models import Usuario,Codigo,Lenguaje,Tipo_Lenguaje,Ejecucion


# Register your models here.
admin.site.register(Usuario)
admin.site.register(Codigo)
admin.site.register(Lenguaje)
admin.site.register(Tipo_Lenguaje)
admin.site.register(Ejecucion)

