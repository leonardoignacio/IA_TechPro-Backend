from django.db import models

# Create your models here.
class Funcionario(models.Model):
    nome = models.charfield('Nome', max_length=50)
    cpf = models.charfield('CPF', max_length=15)
    email = models.charfield('E-mail', max_length=30)
    telefone = models.charfield('Telefone', max_length=15)
    especialidade = models.charfield('Especialidade', max_length=50)
    data_admissao = models.DateField(auto_now_add=True)
    ativo = models.charfield('Ativo', max_length=10)
    salario = models.DecimalField('Salario', max_digits=10, decimal_places=2)
    cargo = models.charfield('Cargo', max_length=50)
    def __str__(self):
        return f'{self.nome} {self.cargo}'
