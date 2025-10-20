from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from django.contrib.auth.models import User
from django.utils.dateformat import format
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response 

# Importe seu modelo
from .models import Equipamento

def _serialize_Equipamento(equipamento):
    return {
         'id': equipamento.id,
        'modelo_marca': equipamento.modelo_marca,
        'patrimonio': equipamento.patrimonio,
        'num_serie': equipamento.num_serie,
    }

@api_view(['GET'])
def py_obter_Equipamentos(request, id_equipamento=None):
    if id_equipamento:
        try:
            equipamento = Equipamento.objects.get(pk=id_equipamento)
            equipamento_data = _serialize_Equipamento(equipamento)
            return Response({'Equipamento': equipamento_data})
        except Equipamento.DoesNotExist:
            return Response({'error': 'Equipamento não encontrado.'}, status=404)
    else:
        equipamento = Equipamento.objects.all()
        equipamento_data = [_serialize_Equipamento(equipamento) for equipamento in equipamento]
        return Response({'equipamento':equipamento_data})