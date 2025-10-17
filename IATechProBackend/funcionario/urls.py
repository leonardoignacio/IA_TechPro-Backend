from django.urls import path
from .views import funcionario

urlpatterns = [
    path('', funcionario, name="funcionario")
]
