from django.contrib import admin
from .models import User

class ListUser(admin.ModelAdmin): 
    list_display = ('id', 'cpf_cnpj','first_name', 'email', 'is_staff') 
    list_display_links = ('id','first_name', 'email') 
    search_fields = ('cpf_cnpj', 'email', 'first_name', 'is_staff') 
    list_per_page = 20 

admin.site.register(User, ListUser)