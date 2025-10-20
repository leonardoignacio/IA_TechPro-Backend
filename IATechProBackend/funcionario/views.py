from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def py_obter_fucnionarios(request):
    return Response({"mensagem": "Funcionario funcionando!"})