from django.db import models

# Create your models here.
class Cultivo(models.Model):
    # Se puede agregar un modelo de terrenos dependiendo del lugar de trabajo,
    # cultivo tendria una fk a terreno  
    nombre = models.CharField(verbose_name='Nombre', max_length=25)
    fecha_siembra = models.DateField(verbose_name='Fecha de siembra', auto_now=True)
    fecha_cosecha = models.DateField(verbose_name='Fecha de cosecha')
    temporada = models.IntegerField(verbose_name='Temporada')
    
    def __str__(self):
        cultivo = f"{self.nombre} (Cosecha del {self.fecha_cosecha})"
        return cultivo
    
class Empleado(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=50)
    apellido = models.CharField(verbose_name='Apellido', max_length=50)
    rut = models.CharField(verbose_name='RUT', max_length=12, default='XXXXXXXX-X')
    sexo = models.CharField(verbose_name='Sexo', max_length=1,
                            choices=[('M', 'Masculino'),
                                     ('F', 'Femenino'),
                                     ('O', 'Otro')])
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    correo = models.EmailField(verbose_name='Correo electrónico', max_length=100)

    def __str__(self):
        empleado = f"{self.nombre} {self.apellido} ({self.rut})"
        return empleado

class Plastico_usado(models.Model):
    cultivo = models.ForeignKey(Cultivo, verbose_name='Cultivo', on_delete=models.CASCADE)
    tipo = models.CharField(verbose_name='Tipo', max_length=50)
    cantidad = models.IntegerField(verbose_name='Cantidad (kg)')
    fecha_uso = models.DateField(verbose_name='Fecha de uso', auto_now=True)
    origen = models.CharField(verbose_name='Origen', max_length=10,
                              choices=[('Nuevo', 'Nuevo'),
                                       ('Reciclado', 'Reciclado')], default='Nuevo')
    def __str__(self):
        plastico_usado = f"{str.capitalize(self.tipo)}"
        return plastico_usado

class Plastico_desechado(models.Model):
    pla_usado = models.ForeignKey(Plastico_usado, verbose_name='Plástico', on_delete=models.CASCADE)
    cantidad = models.IntegerField(verbose_name='Cantidad (kg)')
    fecha_desecho = models.DateField(verbose_name='Fecha de desecho', auto_now=True)
    reciclado = models.BooleanField(verbose_name='¿Plástico reciclado?', default=False)
    # No especifica cuanto del lote es reciclado (se necesita más info)

    def __str__(self):
        plastico_desechado = f"{str.capitalize(self.pla_usado.tipo)} ({self.cantidad}kg)"
        return plastico_desechado