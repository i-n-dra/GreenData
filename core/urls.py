from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('empleados/', views.empleados, name='list_empleados'),
    path('cultivos/', views.cultivos, name='list_cultivos'),
    path('plasticos_usados/', views.pla_usados, name='list_pla_usados'),
    path('plasticos_desechados/', views.pla_desechados, name='list_pla_desechados'),
    # path('empleados/<int:id>', views.empleado_detail, name='detail_empleado')
]
