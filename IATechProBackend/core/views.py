from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from core.models import User
from core.serializers import UserSerializer, RegisterSerializer

def index(request):
    return render(request, 'index.html')

# GET - Lista todos os usuários ou um específico
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def py_obter_usuarios(request, user_id=None):
    if user_id:
        user = get_object_or_404(User, pk=user_id)
        serializer = UserSerializer(user)
        return Response({'user': serializer.data})
    else:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})

# POST - Cria um novo usuário
@api_view(['POST'])
@permission_classes([AllowAny])
def py_criar_usuario(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'status': 'success', 'user_id': user.id}, status=201)
    return Response(serializer.errors, status=400)

# PUT - Atualiza um usuário existente
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def py_edita_usuario(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 'success', 'message': f'Usuário com ID {user_id} atualizado com sucesso.'})
    return Response(serializer.errors, status=400)

# DELETE - Remove um usuário
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def py_deleta_usuario(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return Response({'status': 'success', 'message': f'Usuário com ID {user_id} deletado com sucesso.'})