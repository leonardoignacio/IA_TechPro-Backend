from django.urls import path
from .views import equipamento

urlpatterns = [
    path('api/equipamento', equipamento),
]
