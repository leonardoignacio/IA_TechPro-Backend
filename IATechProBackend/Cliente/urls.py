from django.urls import path
from .views import *

urlpatterns = [
    path('registros/', py_cliente, name="cliente"),
    path('registros/<int:cliente_id>', py_cliente, name="cliente_detalhes"),
    path('cria-cliente', py_cliente_criar, name='cria_cliente'),
    path('deleta/<int:id_cliente>', py_delete_cliente, name='deleta_cliente'),
    path('atualiza/<int:id_cliente>', py_edita_cliente, name='edita_cliente'),
]
