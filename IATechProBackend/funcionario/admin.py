from django.contrib import admin
from .models import Funcionario
# Register your models here.

class FuncionarioAdmin(admin.ModelAdmin):
    list_display=('nome', 'cpf', 'email', 'cargo', 'telefone', 'ativo')
    search_fields=('nome', 'cpf', 'email', 'cargo', 'telefone', 'ativo')
    list_filter=('nome', 'cpf', 'email', 'cargo', 'telefone', 'ativo')

admin.site.register(Funcionario, FuncionarioAdmin)