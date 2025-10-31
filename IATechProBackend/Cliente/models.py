from django.db import models
from core.models import models

# Create your models here.
class Cliente(models.Model):
    data_cadastro = models.DateField(auto_now_add=True)
    keyuser = models.CharField('Keyuser', max_length=50)
    impresa_setor = models.CharField('Cargo', max_length=50)

    def __str__(self):
        return f'{self.nome} {self.email}'