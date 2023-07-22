from django.contrib import admin
from .models import LocalesComida, LocalesRepuestos, Barrio, Persona

# Register your models here.

admin.site.register(Barrio)
admin.site.register(Persona)
admin.site.register(LocalesComida)
admin.site.register(LocalesRepuestos)
