from django.db import models
from core.models import User

# Create your models here.
class Cliente(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    empresa = models.CharField('Empresa', max_length=50)
    setor = models.CharField('Setor', max_length=50)

    def __str__(self):
        return f'{self.nome} {self.email}'