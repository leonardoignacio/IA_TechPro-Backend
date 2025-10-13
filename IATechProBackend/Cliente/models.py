from django.db import models

# Create your models here.
class Cliente(models.Model):
    ativo = models.CharField('Ativo', max_Length=10)
    nome = models.CharField('Nome',max_Length=50)
    cep = models.CharField('CEP', max_Length=10)
    data_cadastro = models.DateField(auto_now_add=True)
    email = models.CharField('E-mail', max_Length=30)
    telefone = models.CharField('Telefone', max_Length=15)
    estado = models.CharField('Estado', max_length=2)
    endereco = models.CharField('Endereço', max_Length=50)
    cpf_cnpj = models.CharField('CPF/CNPJ', max_Length=16)
    cidade = models.CharField('Cidade', max_Length=50)
    def __str__(self):
        return f'{self.nome} {self.email}'