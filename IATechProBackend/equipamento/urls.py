from django.urls import path
from .views import *

urlpatterns = [
    path('registros/', py_obter_Equipamentos, name="equipamento"),
    path('registros/<int:id_equipamento>', py_obter_Equipamentos, name="equipamento_detalhe")
]
