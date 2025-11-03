from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Informações adicionais', {
            'fields': ('cpf_cnpj', 'telefone', 'logradouro', 'cep', 'cidade', 'estado')
        }),
    )
    list_display = ('username', 'email', 'cpf_cnpj', 'telefone', 'cidade', 'estado', 'is_staff')
    search_fields = ('username', 'email', 'cpf_cnpj', 'cidade', 'estado')