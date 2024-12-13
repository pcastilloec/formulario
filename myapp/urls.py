from django.urls import path
from . import views

urlpatterns = [
    path('', views.registro_list, name='registro_list'),
    path('nuevo/', views.registro_racks, name='registro_racks'),
    path('nuevomq/', views.registro_maquinas, name='registro_maquinas'),
    path('visualizar/', views.visualizar_registros_racks, name='visualizar_registros_racks'),
    path('visualizarmq/', views.visualizar_registros_maquinas, name='visualizar_registros_maquinas'),
    path('reporte-toneladas/', views.reporte_detallado, name='reporte_detallado'),

]

    #path('respaldo',views.respaldo, name='respaldo_registro' ),
    #path('editar/<int:pk>/', views.registro_update, name='registro_update'),
    #path('eliminar/<int:pk>/', views.registro_delete, name='registro_delete'),
    #path('nuevo/<str:RCKS>/', views.registro_racks, name='registro_racks'),


