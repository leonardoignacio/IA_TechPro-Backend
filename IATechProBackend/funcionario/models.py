from django.db import models

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField('Nome', max_length=50)
    cpf = models.CharField('CPF', max_length=15)
    email = models.CharField('E-mail', max_length=30)
    telefone = models.CharField('Telefone', max_length=15)
    especialidade = models.CharField('Especialidade', max_length=50)
    data_admissao = models.DateField(auto_now_add=True)
    ativo = models.CharField('Ativo', max_length=10)
    salario = models.DecimalField('Salario', max_digits=10, decimal_places=2)
    cargo = models.CharField('Cargo', max_length=50)
    def __str__(self):
        return f'{self.nome} {self.cargo}'
