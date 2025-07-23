from django.shortcuts import render
from .models import Cultivo, Empleado, Plastico_desechado, Plastico_usado
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.http import Http404, HttpRequest, HttpResponse

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

class empleados_crear(CreateView):
    model = Empleado
    template_name = 'empleados/create_empleados.html'
    fields = [
        'nombre',
        'apellido',
        'sexo',
        'fecha_nacimiento',
        'correo',
        'rut'
    ]
    success_url = reverse_lazy('list_empleados')
    def get(self, request):
        self.object = None
        return super().get(request)
    
    def form_valid(self, form):
        return super().form_valid(form)
    
class empleados_actualizar(UpdateView):
    model = Empleado
    template_name = 'empleados/update_empleados.html'
    fields = [
        'nombre',
        'apellido',
        'sexo',
        'fecha_nacimiento',
        'correo',
        'rut'
    ]
    success_url = reverse_lazy('list_empleados')

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)

        return queryset.get()

class empleados_eliminar(DeleteView):
    model = Empleado
    template_name = 'empleados/delete_empleados.html'
    success_url = reverse_lazy('list_empleados')
    context_object_name = 'empleado'
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)

        return queryset.get()

def cultivos(request):
    cultivos = Cultivo.objects.all()
    context = {'cultivos': cultivos}
    return render(request, 'list_cultivos.html', context=context)

class cultivos_crear(CreateView):
    model = Cultivo
    template_name = 'cultivos/create_cultivos.html'
    fields = [
        'nombre',
        'temporada'
    ]
    success_url = reverse_lazy('list_cultivos')
    def get(self, request):
        self.object = None
        return super().get(request)
    
    def form_valid(self, form):
        return super().form_valid(form)

class cultivos_actualizar(UpdateView):
    model = Cultivo
    template_name = 'cultivos/update_cultivos.html'
    fields = [
        'nombre',
        'fecha_cosecha',
        'temporada'
    ]
    success_url = reverse_lazy('list_cultivos')

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)

        return queryset.get()

class cultivos_eliminar(DeleteView):
    model = Cultivo
    template_name = 'cultivos/delete_cultivos.html'
    success_url = reverse_lazy('list_cultivos')
    context_object_name = 'cultivo'
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)

        return queryset.get()

def pla_usados(request):
    pla_usados = Plastico_usado.objects.all()
    context = {'pla_usados': pla_usados}
    return render(request, 'list_pla_usados.html', context=context)

def pla_desechados(request):
    pla_desechados = Plastico_desechado.objects.all()
    context = {'pla_desechados': pla_desechados}
    return render(request, 'list_pla_desechados.html', context=context)