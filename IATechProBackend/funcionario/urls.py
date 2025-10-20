from django.urls import path
from .views import *

urlpatterns = [
<<<<<<< HEAD
    path('registros/', py_obter_funcionarios, name="funcionario"),
    path('registros/<int:funcionario_id>', py_obter_funcionarios, name="funcionario_detalhe")
=======
    path('', py_obter_fucnionarios, name="funcionario")
>>>>>>> 218e9aaf81ffe54500d4dad784f09ba8fa7e8ee1
]
