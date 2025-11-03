from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db import transaction

from funcionario.models import Funcionario
from funcionario.serializers import FuncionarioSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_funcionarios(request, funcionario_id=None):
    if funcionario_id:
        funcionario = get_object_or_404(Funcionario, pk=funcionario_id)
        serializer = FuncionarioSerializer(funcionario)
        return Response({'funcionario': serializer.data})
    
    funcionarios = Funcionario.objects.all()
    serializer = FuncionarioSerializer(funcionarios, many=True)
    return Response({'funcionarios': serializer.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def criar_funcionario(request):
    serializer = FuncionarioSerializer(data=request.data)
    if serializer.is_valid():
        with transaction.atomic():
            serializer.save(user=request.user)
        return Response({'status': 'success', 'funcionario': serializer.data}, status=status.HTTP_201_CREATED)
    return Response({'status': 'error', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def editar_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, pk=funcionario_id)
    serializer = FuncionarioSerializer(funcionario, data=request.data, partial=True)
    if serializer.is_valid():
        with transaction.atomic():
            serializer.save()
        return Response({'status': 'success', 'funcionario': serializer.data})
    return Response({'status': 'error', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deletar_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, pk=funcionario_id, user=request.user)
    with transaction.atomic():
        funcionario.delete()
    return Response({'status': 'success', 'message': f'Funcionário {funcionario_id} deletado com sucesso.'})
