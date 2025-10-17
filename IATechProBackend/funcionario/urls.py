from django.urls import path
from funcionario.views import index

urlpatterns = [
    path('api/funcionario', index)
]
