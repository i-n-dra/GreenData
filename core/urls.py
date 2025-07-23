from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('empleados/', views.empleados, name='list_empleados'),
    path('cultivos/', views.cultivos, name='list_cultivos'),
    path('plasticos_usados/', views.pla_usados, name='list_pla_usados'),
    path('plasticos_desechados/', views.pla_desechados, name='list_pla_desechados'),
    # path('empleados/<int:id>', views.empleado_detail, name='detail_empleado')
    path('empleados/crear/', views.empleados_crear.as_view(), name='create_empleado'),
    path('empleados/actualizar/<int:pk>/', views.empleados_actualizar.as_view(), name='update_empleado'),
    path('empleados/eliminar/<int:pk>/', views.empleados_eliminar.as_view(), name='delete_empleado'),
    path('cultivos/crear/', views.cultivos_crear.as_view(), name='create_cultivo'),
    path('cultivos/actualizar/<int:pk>/', views.cultivos_actualizar.as_view(), name='update_cultivo'),
    path('cultivos/eliminar/<int:pk>/', views.cultivos_eliminar.as_view(), name='delete_cultivo')
]
