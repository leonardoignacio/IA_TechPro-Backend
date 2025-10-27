from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from django.contrib.auth.models import User
from django.utils.dateformat import format
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from funcionario.models import Funcionario

def _serialize_funcionarios(funcionario):
    return  {
        'id': funcionario.id,
        'nome': funcionario.nome,
        'cpf': funcionario.cpf,
        'email': funcionario.email,
        'telefone': funcionario.telefone,
        'especialidade': funcionario.especialidade,
        'data_admissao': format(funcionario.data_admissao, 'Y-m-d'),
        'salario': funcionario.salario,
        'cargo': funcionario.cargo,
        'ativo' : funcionario.ativo,
    }

# Create your views here.
@api_view(['GET'])
def py_obter_funcionarios(request, funcionario_id=None):
    if funcionario_id:
        try:
            funcionario = Funcionario.objects.get(pk=funcionario_id)
            funcionario_data = _serialize_funcionarios(funcionario)
            return Response({'funcionario': funcionario_data})
        except Funcionario.DoesNotExist:
            return Response({'error': 'Funcionario não encontrado.'}, status=404)
    else:
        funcionarios = Funcionario.objects.all()
        funcionarios_data = [_serialize_funcionarios(funcionario) for funcionario in funcionarios]
        return Response({'funcionarios': funcionarios_data})    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def py_cria_funcionarios(request):
    data = request.data
    funcionario = Funcionario.objects.create(
        nome=data.get('nome'),
        cpf=data.get('cpf'),
        email=data.get('email'),
        telefone=data.get('telefone'),
        especialidade=data.get('especialidade'),
        data_admissao=data.get('data_admissao'),
        salario=data.get('salario'),
        cargo=data.get('cargo'),
        ativo=data.get('ativo', True)
    )
    return Response({'status': 'success', 'funcionario_id': funcionario.id}, status=201)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def py_deleta_funcionarios(request, funcionario_id):
    """
    Função para deletar um funcionario específico.
    O usuário só pode deletar seus próprios funcionarios
    """

    funcionario = get_object_or_404(Funcionario, pk=funcionario_id, funcionario=request.user)
    funcionario.delete()
    return Response({'status': 'success', 'message': f'Funcionario com ID {funcionario_id} deletado com sucesso.'})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def py_edita_funcionarios(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, pk=funcionario_id)
    data = request.data
    # Atualiza apenas os campos presentes no JSON
    funcionario.nome=data.get('nome', funcionario.nome )
    funcionario.cpf=data.get('cpf' ,funcionario.cpf )
    funcionario.email=data.get('email', funcionario.email )
    funcionario.telefone=data.get('telefone', funcionario.telefone )
    funcionario.especialidade=data.get('especialidade', funcionario.especialidade )
    funcionario.data_admissao=data.get('data_admissao', funcionario.data_admissao )
    funcionario.salario=data.get('salario', funcionario.salario )
    funcionario.cargo=data.get('cargo', funcionario.cargo )
    funcionario.ativo=data.get('ativo', funcionario.ativo)
    funcionario.save()
    return Response({'status': 'success', 'message': f'Funcionario com ID {funcionario_id} atualizado com sucesso.'})
