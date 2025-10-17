from django.urls import path
from .views import funcionario

urlpatterns = [
    path('api/funcionario', funcionario)
]
