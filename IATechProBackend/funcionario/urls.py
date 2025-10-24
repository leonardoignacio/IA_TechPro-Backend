from django.urls import path
from .views import *

urlpatterns = [
    path('registros/', py_obter_funcionarios, name="funcionario"),
    path('registros/<int:funcionario_id>', py_obter_funcionarios, name="funcionario_detalhe")
]
