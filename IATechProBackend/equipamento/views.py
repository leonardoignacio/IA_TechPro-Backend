from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def equipamento(request):
    return Response({"mensagem": "Equipamento funcionando!"})

