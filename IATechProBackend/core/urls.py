from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    #path('user-auth/', current_user_view, name='current-user'),

    # Novas rotas para o modelo User
    path('usuarios/', py_obter_usuarios, name='listar-usuarios'),
    path('usuarios/<int:user_id>/', py_obter_usuarios, name='detalhar-usuario'),
    path('usuarios/criar/', py_criar_usuario, name='criar-usuario'),
    path('usuarios/<int:user_id>/editar/', py_edita_usuario, name='editar-usuario'),
    path('usuarios/<int:user_id>/deletar/', py_deleta_usuario, name='deletar-usuario'),
]