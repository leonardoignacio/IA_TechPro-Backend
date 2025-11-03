from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Cliente

from .serializers import serialize_cliente

@api_view(['GET'])
def py_cliente(request, cliente_id=None):
    if cliente_id:
        cliente = get_object_or_404(Cliente, pk=cliente_id)
        return Response({'cliente': serialize_cliente(cliente)})
    else:
        clientes = Cliente.objects.all()
        return Response({'clientes': [serialize_cliente(c) for c in clientes]})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def py_cliente_criar(request):
    data = request.data
    cliente = Cliente.objects.create(
        empresa=data.get('empresa'),
        setor=data.get('setor'),
        user=data.get('user') #request.user  
    )
    return Response({'status': 'success', 'id_cliente': cliente.id}, status=201)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def py_delete_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, pk=id_cliente, user=request.user)
    cliente.delete()
    return Response({'status': 'success', 'message': f'Cliente com ID {id_cliente} deletado com sucesso.'})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def py_edita_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, pk=id_cliente)
    data = request.data

    cliente.empresa = data.get('empresa', cliente.empresa)
    cliente.setor = data.get('setor', cliente.setor)
    cliente.save()

    return Response({'status': 'success', 'message': f'Cliente com ID {id_cliente} atualizado com sucesso.'})