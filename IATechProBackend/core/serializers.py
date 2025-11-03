from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'email',
            'cpf_cnpj',
            'telefone',
            'logradouro',
            'cep',
            'cidade',
            'estado',
        )

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'first_name',
            'email',
            'cpf_cnpj',
            'telefone',
            'logradouro',
            'cep',
            'cidade',
            'estado',
        )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user