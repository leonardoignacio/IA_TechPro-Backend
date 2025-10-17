from django.urls import admin
from .views import cliente

urlpatterns = [
    path('api/cliente', cliente)
]