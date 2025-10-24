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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def py_cliente(request):
    data = request.data
    cliente = Cliente.objects.create(
        ativo=data.get('ativo', True),
        nome=data.get('nome'),
        cep=data.get('cep'),
        data_cadastro=data.get('data_cadastro'),
        email=data.get('email'),
        telefone=data.get('telefone'),
        estado=data.get('estado'),
        endereco=data.get('endereco'),
        cpf_cnpj=data.get('cpf_cnpj'),
        cidade=data.get('cidade'),
    )
    return Response({'status': 'success', 'id_cliente': id.cliente}, status=201)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def py_delete_cliente(request, id_cliente):
    """
    Função para deletear um prato específico.
    """
    cliente = get_object_or_404(Cliente, pk=id_cliente)
    cliente.delete()
    return Response({'status': 'success', 'message': f'Cliente com ID {id_cliente} deletado com sucesso.'})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def py_edita_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, pk=id_cliente)
    data = request.data
    # Atualiza apenas os campos presentes no JSON
    cliente.ativo = data.get('ativo', cliente.ativo)
    cliente.nome = data.get('nome', cliente.nome)
    cliente.cep = data.get('cep', cliente.cep)
    cliente.data_cadastro = data.get('data_cadastro', cliente.data_cadastro)
    cliente.email = data.get('email', cliente.email)
    cliente.telefone = data.get('telefone', cliente.telefone)
    cliente.estado = data.get('estado', cliente.estado)
    cliente.endereco = data.get('endereco', cliente.endereco)
    cliente.cpf_cnpj = data.get('cpf_cnpj', cliente.cpf_cnpj)
    cliente.cidade = data.get('cidade', cliente.cidade)
    cliente.save()
    return Response({'status': 'success', 'message': f'Cliente com ID {id_cliente} atualizado com sucesso.'})