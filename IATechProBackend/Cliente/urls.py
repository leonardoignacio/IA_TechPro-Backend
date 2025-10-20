from django.urls import path
from .views import *

urlpatterns = [
    path('registros/', py_cliente, name="cliente"),
    path('registros/<int:cliente_id>', py_cliente, name="cliente_detalhes")
]
