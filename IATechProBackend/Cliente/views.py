from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from django.contrib.auth.models import User
from django.utils.dateformat import format
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

# Importando modelo CLiente de models.py
from .models import Cliente

def _serialize(cliente):
    return {
        'id': cliente.id,
        'ativo': cliente.ativo,
        'nome': cliente.nome,
        'cep': cliente.cep,
        'data_cadastro': cliente.data_cadastro,
        'email': cliente.email,
        'telefone': cliente.telefone,
        'estado': cliente.estado,
        'endereco': cliente.endereco,
        'cpf_cnpj': cliente.cpf_cnpj,
        'cidade': cliente.cidade,
    }

@api_view(['GET'])
def py_cliente(request, cliente_id=None):
    if cliente_id:
        try:
            cliente = Cliente.objects.get(pk=cliente_id)
            cliente_data = _serialize(cliente)
            return Response({'cliente': cliente_data})
        except Cliente.DoesNotExist:
            return Response({'error': 'Cliente não encontrado.'}, status=404)
    else:
        cliente = Cliente.objects.all()
        cliente_data = [_serialize(cliente) for cliente in cliente]
        return Response({'clientes': cliente_data})
