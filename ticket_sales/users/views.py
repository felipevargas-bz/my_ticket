from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.serializers import UserSerializer, UserRegistrationSerializer

# Create your views here.


class UserRegistration(APIView):

    def post(self, request):
        data = request.data
        serializer = UserRegistrationSerializer(data=data)
        if serializer.is_valid():
            serializer.create(validated_data=data)
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class UserDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        # Obtener el usuario mediante el token de autenticación
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=200)
