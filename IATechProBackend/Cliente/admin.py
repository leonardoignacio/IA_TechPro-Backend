from django.contrib import admin
from .models import Cliente

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display=('ativo','Nome','CEP','E-mail','Telefone','Estado','CPF/CNPJ','Cidade')
    search_fields=('ativo','Nome','CEP','E-mail','Telefone','Estado','CPF/CNPJ','Cidade')
    list_filter=('ativo','Nome','CEP','E-mail','Telefone','Estado','CPF/CNPJ','Cidade')

admin.site.register(Cliente, ClienteAdmin)