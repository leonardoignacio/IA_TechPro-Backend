from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Cliente

def serialize_cliente(cliente):
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
def listar_clientes(request, cliente_id=None):
    if cliente_id:
        cliente = get_object_or_404(Cliente, pk=cliente_id)
        return Response({'cliente': serialize_cliente(cliente)})
    clientes = Cliente.objects.all()
    return Response({'clientes': [serialize_cliente(c) for c in clientes]})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def criar_cliente(request):
    data = request.data
    cliente = Cliente.objects.create(
        ativo=data.get('ativo', True),
        nome=data.get('nome'),
        cep=data.get('cep'),
        email=data.get('email'),
        telefone=data.get('telefone'),
        estado=data.get('estado'),
        endereco=data.get('endereco'),
        cpf_cnpj=data.get('cpf_cnpj'),
        cidade=data.get('cidade'),
    )
    return Response({'status': 'sucesso', 'id_cliente': cliente.id}, status=201)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def atualizar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, pk=id_cliente)
    data = request.data

    for campo in [
        'ativo', 'nome', 'cep', 'email', 'telefone',
        'estado', 'endereco', 'cpf_cnpj', 'cidade'
    ]:
        if campo in data:
            setattr(cliente, campo, data[campo])

    cliente.save()
    return Response({'status': 'sucesso', 'mensagem': f'Cliente {cliente.id} atualizado com sucesso.'})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deletar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, pk=id_cliente)
    cliente.delete()
    return Response({'status': 'sucesso', 'mensagem': f'Cliente {id_cliente} deletado com sucesso.'})