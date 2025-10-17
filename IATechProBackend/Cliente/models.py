from django.db import models

# Create your models here.
class Cliente(models.Model):
    ativo = models.CharField('Ativo', max_length=10)
    nome = models.CharField('Nome',max_length=50)
    cep = models.CharField('CEP', max_length=10)
    data_cadastro = models.DateField(auto_now_add=True)
    email = models.EmailField('E-mail', max_length=30, unique=True)
    telefone = models.CharField('Telefone', max_length=15)
    estado = models.CharField('Estado', max_length=2)
    endereco = models.CharField('Endereço', max_length=50)
    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=16)
    cidade = models.CharField('Cidade', max_length=50)
    def __str__(self):
        return f'{self.nome} {self.email}'