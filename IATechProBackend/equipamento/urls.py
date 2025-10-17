from django.urls import path
from equipamento.views import index

urlpatterns = [
    path('api/equipamento', index),
]
