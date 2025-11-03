from django.urls import path
from .views import *

urlpatterns = [
    path('registros/', listar_funcionarios, name="funcionario"),
    path('registros/<int:funcionario_id>', listar_funcionarios, name="funcionario_detalhe"),
    path('cria-funcionario', criar_funcionario, name="cria_funcionario"),
    path('deleta/<int:funcionario_id>', deletar_funcionario, name="deleta_funcionario"),
    path('atualiza/<int:funcionario_id>', editar_funcionario, name="edita_funcionario"),
]
