from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from django.utils.dateformat import format
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import OrdemdeServico
# Create your views here.

def _serialize(OrdemdeServico):
    return {
        'data_de_conclusao': OrdemdeServico.data_conclusao,
        'status': OrdemdeServico.status,
        'data_criacao': OrdemdeServico.data_criacao,
        'prioridade': OrdemdeServico.prioridade,
        'observacao': OrdemdeServico.observacao,
        'diagnostico': OrdemdeServico.diagnostico,
        'categoria': OrdemdeServico.categoria,
        'problema_relatado': OrdemdeServico.problema_relatado,
        'valor_servico': OrdemdeServico.valor_servico,
        'cliente': OrdemdeServico.cliente,
        'equipamento': OrdemdeServico.equipamento,
        'funcionario': OrdemdeServico.funcionario,
    }  



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ordemservico_pyCriar(request):
    data = request.data
    ordemservico = OrdemdeServico.objects.create(
        data_de_conclusao=data.get('data_de_conclusao'),
        status=data.get('status'),
        data_criacao=data.get('data_criacao'),
        prioridade=data.get('prioridade'),
        observacao=data.get('observacao'),
        diagnostico=data.get('diagnostico'),
        categoria=data.get('categoria'),
        problema_relatado=data.get('problema_relatado'),
        valor_servico=data.get('valor_servico'),
        cliente=data.get('cliente'),
        equipamento=data.get('equipamento'),
        funcionario=request.user #Associa a OS ao usuário logado,
    )
    return Response({"mensagem": "OSs funcionando!"})


@api_view(['GET'])
def py_OrdemdeServico(request, id_ordem=None):
    if id_ordem:
        try:
            OrdemdeServico = OrdemdeServico.objects.get(pk=id_ordem)
            OrdemdeServico_data = _serialize(OrdemdeServico)
            return Response({'Ordem': id_ordem})
        except OrdemdeServico.DoesNotExist:
            return Response({'error': 'Ordem não encontrado.'}, status=404)
    else:
        OrdemdeServico = OrdemdeServico.objects.all()
        OrdemdeServico = [_serialize(OrdemdeServico) for OrdemdeServico in OrdemdeServico]
        return Response({'Ordem': id_ordem})



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def py_delete_OrdemdeServico(request, id_ordem):

    OrdemdeServico = get_object_or_404(OrdemdeServico, pk=id_ordem)
    OrdemdeServico.delete()
    return Response({'status': 'success', 'message': f'Ordem de serviço {id_ordem} deletado com sucesso.'})


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def py_edita_OrdemdeServico(request, id_ordem):
    OrdemdeServico = get_object_or_404(OrdemdeServico, pk=id_ordem)
    data = request.data
    # Atualiza apenas os campos presentes no JSON
    OrdemdeServico.data_de_conclusao = data.get('Conclusão', OrdemdeServico.data_de_conclusao)
    OrdemdeServico.status = data.get('Status', OrdemdeServico.status)
    OrdemdeServico.data_criacao = data.get('Data da Criação', OrdemdeServico.data_criacao)
    OrdemdeServico.prioridade = data.get('Prioridade', OrdemdeServico.prioridade)
    OrdemdeServico.observacao = data.get('Observação', OrdemdeServico.observacao)
    OrdemdeServico.diagnostico = data.get('diagnostico', OrdemdeServico.diagnostico)
    OrdemdeServico.categoria = data.get('Categoria', OrdemdeServico.categoria)
    OrdemdeServico.problema_relatado = data.get('Problema', OrdemdeServico.problema_relatado)
    OrdemdeServico.valor_servico = data.get('Valor', OrdemdeServico.valor_servico)
    OrdemdeServico.cliente = data.get('cliente', OrdemdeServico.cliente)
    OrdemdeServico.equipamento = data.get('equipamento', OrdemdeServico.equipamento)
    OrdemdeServico.funcionario = data.get('funcionario', OrdemdeServico.funcionario)
    OrdemdeServico.save()
    return Response({'status': 'success', 'message': f'Ordem com ID {id_ordem} atualizado com sucesso.'})


