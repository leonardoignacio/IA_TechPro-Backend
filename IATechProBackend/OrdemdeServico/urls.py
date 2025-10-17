from django.contrib import admin
from .views import ordemservico

urlpatterns = [
    path('api/os', ordemservico)
]
