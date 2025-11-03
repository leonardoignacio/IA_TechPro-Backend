from django.db import models
from django.utils.translation import gettext_lazy as _

class Cliente(models.Model):
    # Dados pessoais
    nome = models.CharField(_('Nome'), max_length=50)
    cpf_cnpj = models.CharField(_('CPF/CNPJ'), max_length=16, help_text=_('Informe o CPF ou CNPJ do cliente'))
    data_cadastro = models.DateField(_('Data de Cadastro'), auto_now_add=True)
    ativo = models.BooleanField(_('Ativo'), default=True)

    # Contato
    email = models.EmailField(_('E-mail'), max_length=30, unique=True, help_text=_('E-mail principal do cliente'))
    telefone = models.CharField(_('Telefone'), max_length=15)

    # Endereço
    cep = models.CharField(_('CEP'), max_length=10)
    endereco = models.CharField(_('Endereço'), max_length=50)
    cidade = models.CharField(_('Cidade'), max_length=50)
    estado = models.CharField(_('Estado'), max_length=2)

    class Meta:
        verbose_name = _('Cliente')
        verbose_name_plural = _('Clientes')
        ordering = ['nome']

    def __str__(self):
        return f'{self.nome} ({self.email})'
