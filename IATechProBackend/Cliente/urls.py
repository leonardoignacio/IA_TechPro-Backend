from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('registros/', views.py_cliente, name='lista_clientes'),
    path('registros/<int:cliente_id>/', views.py_cliente, name='detalhes_cliente'),
    path('criar/', views.py_cliente_criar, name='criar_cliente'),
    path('deletar/<int:id_cliente>/', views.py_delete_cliente, name='deletar_cliente'),
    path('atualizar/<int:id_cliente>/', views.py_edita_cliente, name='atualizar_cliente'),
]
