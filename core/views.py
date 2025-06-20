from django.shortcuts import render
from .models import Cultivo, Empleado, Plastico_desechado, Plastico_usado

# Create your views here.
def home(request):
    cultivos = Cultivo.objects.all
    c_count = Cultivo.objects.count()
    c_format = f"{int(c_count):,}".replace(',', '.')
    # https://docs.python.org/3/library/string.html#format-string-syntax:~:text=%27%2C%27,is%20not%20supported.
    
    empleados = Empleado.objects.all

    pla_usados_count = 0
    for p in Plastico_usado.objects.all():
        pla_usados_count += p.cantidad
    pu_format = f"{int(pla_usados_count):,}".replace(',', '.')
    
    pla_desechados_count = 0
    for p in Plastico_desechado.objects.all():
        pla_desechados_count += p.cantidad
    pd_format = f"{int(pla_desechados_count):,}".replace(',', '.')

    context = {'cultivos': cultivos,
               'c_format': c_format,
               'empleados': empleados,
               'pla_usados': pu_format,
               'pla_desechados': pd_format}
    return render(request,'home.html', context=context)

def empleados(request):
    empleados = Empleado.objects.all()
    context = {'empleados': empleados}
    return render(request, 'list_empleados.html', context=context)

def cultivos(request):
    cultivos = Cultivo.objects.all()
    context = {'cultivos': cultivos}
    return render(request, 'list_cultivos.html', context=context)

def pla_usados(request):
    pla_usados = Plastico_usado.objects.all()
    context = {'pla_usados': pla_usados}
    return render(request, 'list_pla_usados.html', context=context)

def pla_desechados(request):
    pla_desechados = Plastico_desechado.objects.all()
    context = {'pla_desechados': pla_desechados}
    return render(request, 'list_pla_desechados.html', context=context)