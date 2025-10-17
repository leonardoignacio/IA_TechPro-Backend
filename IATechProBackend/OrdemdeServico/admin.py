from django.contrib import admin
from .models import OrdemdeServico

# Register your models here.
class Ordemservicoadmin(admin.Modeladmin):
    list_display=('prioridade', 'status', 'data_criacao')
    search_files=('observacao', ' data_de_conclusao', 'categoria')
    list_filter=('diagnostico', 'categoria', 'problema_relatado')
admin.site.register(OrdemdeServico, Ordemservicoadmin)
