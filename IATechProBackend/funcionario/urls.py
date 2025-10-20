from django.urls import path
from .views import *

urlpatterns = [
    path('', py_obter_fucnionarios, name="funcionario")
]
