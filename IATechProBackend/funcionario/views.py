from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from django.contrib.auth.models import User
from django.utils.dateformat import format
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from funcionario.models import Funcionario

def _serialize_funcionario(funcionario):
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
    }



# Create your views here.
@api_view(['GET'])
def py_obter_funcionarios(request, funcionario_id=None):
    if funcionario_id:
        try:
            funcionario = Funcionario.objects.get(pk=funcionario_id)
            funcionario_data = _serialize_funcionario(funcionario)
            return Response({'funcionario': funcionario_data})
        except Funcionario.DoesNotExist:
            return Response({'error': 'Funcionario não encontrado.'}, status=404)
    else:
        funcionarios = Funcionario.objects.all()
        funcionarios_data = [_serialize_funcionario(funcionario) for funcionario in funcionarios]
        return Response({'funcionarios': funcionarios_data})    



