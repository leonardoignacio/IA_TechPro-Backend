from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
fgrom django.contrib.auth.models import User
from django.utils.dateformat import format
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response 

# Importe seu modelo
from .models import Equipamento

def _serialize_Equipamento(Equipamento):
    return {
         'id': Equipamento.id_equipamento,
        'modelo_marca': Equipamento.modelo_marca,
        'patrimonio': Equipamento.patrimonio,
        'num_serie': Equipamento.num_serie,
    }

@api_view(['GET'])
def py_obter_Equipamentos(request, id_equipamento=None):
    if id_equipamento:
        try:
            Equipamento = Equipamento.objects.get(pk=id_equipamento)
            Equipamento_data = _serialize_Equipamento(Equipamento)
            return Response({'Equipamento': Equipamento_data})
        except Equipamento.DoesNotExist:
            return Response({'error': 'Equipamento não encontrado.'}, status=404)
        else:
            Equipamento = Equipamento.objects_all()
            Equipamento_data = [_serialize_Equipamento(Equipamento) for Equipamento in Equipamento]
            return Response({'Equipamento:' Equipamento_data})