from django.urls import path
from .views import ordemservico

urlpatterns = [
    path('', ordemservico, name="os")
]
