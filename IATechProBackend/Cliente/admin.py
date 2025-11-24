
from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user__username','user__first_name', 'empresa', 'setor', 'user')
    search_fields = ('empresa', 'setor', 'user__username')
    list_filter = ('user__username','user__first_name','setor', 'empresa')
