from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'cidade', 'estado', 'ativo')
    list_display_links = ('nome',)
    search_fields = ('nome', 'email', 'telefone', 'cidade')
    list_filter = ('ativo', 'estado', 'cidade')
    readonly_fields = ('data_cadastro',)
    date_hierarchy = 'data_cadastro'

    fieldsets = (
        (_('Dados Pessoais'), {
            'fields': ('nome', 'cpf_cnpj', 'data_cadastro', 'ativo')
        }),
        (_('Contato'), {
            'fields': ('email', 'telefone')
        }),
        (_('Endereço'), {
            'fields': ('cep', 'endereco', 'cidade', 'estado')
        }),
    )
