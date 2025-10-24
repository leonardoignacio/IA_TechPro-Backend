from django.urls import path
from .views import *

urlpatterns = [
    path('registros/', py_obter_funcionarios, name="funcionario"),
    path('registros/<int:funcionario_id>', py_obter_funcionarios, name="funcionario_detalhe"),
    path('cria-funcionario', py_cria_funcionarios, name="cria_funcionario"),
    path('deleta/<int:funcionario_id>', py_deleta_funcionarios, name="deleta_funcionario"),
    path('edita/<int:funcionario_id>', py_edita_funcionarios, name="edita_funcionario"),
]
