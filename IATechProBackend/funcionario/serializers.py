from rest_framework import serializers
from funcionario.models import Funcionario

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['id', 'especialidade', 'data_admissao', 'salario', 'cargo', 'user']
        read_only_fields = ['id', 'user']
