from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserSerializer
from .permissions import IsAdmin, IsStaff

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class MeView(APIView):
    def get(self, request):
        return Response(UserSerializer(request.user).data)

class AdminOnlyView(APIView):
    permission_classes = [IsAdmin]
    def get(self, request):
        return Response({"message": "Solo admin puede ver esto"})

class StaffOnlyView(APIView):
    permission_classes = [IsStaff]
    def get(self, request):
        return Response({"message": "Admin y Staff pueden ver esto"})
