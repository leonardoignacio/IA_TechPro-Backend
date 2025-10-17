from django.contrib import admin
from .models import Cliente

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display=('ativo','nome','cep','email','telefone','estado','cpf_cnpj','cidade')
    search_fields=('ativo','nome','cep','email','telefone','estado','cpf_cnpj','cidade')
    list_filter=('ativo','nome','cep','email','telefone','estado','cpf_cnpj','cidade')

admin.site.register(Cliente, ClienteAdmin)