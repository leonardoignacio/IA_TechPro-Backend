from django.db import models
from core.models import User
# Create your models here.
class Funcionario(models.Model):
    especialidade = models.CharField('Especialidade', max_length=50)
    data_admissao = models.DateField(auto_now_add=True)
    salario = models.DecimalField('Salario', max_digits=10, decimal_places=2)
    cargo = models.CharField('Cargo', max_length=50)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f'{self.nome} {self.cargo}'
