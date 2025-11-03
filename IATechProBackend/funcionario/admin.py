from django.contrib import admin
from .models import Funcionario

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'especialidade', 'cargo', 'salario', 'data_admissao', 'user')
    list_display_links = ('id', 'especialidade', 'cargo')
    search_fields = ('especialidade', 'cargo', 'user__first_name', 'user__email')
    list_filter = ('especialidade', 'cargo', 'data_admissao')
    ordering = ('-data_admissao',)
    list_per_page = 25
