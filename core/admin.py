from django.contrib import admin
from .models import Cultivo, Empleado, Plastico_usado, Plastico_desechado

# Register your models here.
admin.site.register(Cultivo)
admin.site.register(Empleado)
admin.site.register(Plastico_usado)
admin.site.register(Plastico_desechado)