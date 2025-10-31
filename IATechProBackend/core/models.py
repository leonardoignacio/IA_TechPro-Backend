from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ativo = models.BooleanField(default=True)
    nome = models.CharField('Nome', max_length=50)
    cpf_cnpj = models.CharField(max_length=200, unique=True) 
    email = models.EmailField('E-mail', max_length=30, unique=True)
    telefone = models.CharField('Telefone', max_length=15)
    logradouro = models.CharField('Logradouro',max_length=200)
    cep = models.CharField('CEP', max_length=10)
    cidade = models.CharField('Cidade', max_length=50)
    estado = models.CharField('Estado', max_length=2)
    