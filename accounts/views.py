from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Skill
from .serializers import UserSerializer, SkillSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = []


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            # Admins can see all users
            return User.objects.all()
        # Normal users can only see themselves
        return User.objects.filter(id=user.id)

    def perform_create(self, serializer):
        user = self.request.user
        if user.role != 'admin':
            raise PermissionDenied("Only admins can create users")
        serializer.save()

    def perform_update(self, serializer):
        user = self.request.user
        # Normal users can update only their own profile
        if user.role != 'admin' and serializer.instance != user:
            raise PermissionDenied("You can only update your own profile")
        serializer.save()

    def perform_destroy(self, instance):
        user = self.request.user
        if user.role != 'admin':
            raise PermissionDenied("Only admins can delete users")
        instance.delete()


class UserSelfDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        user.delete()
        return Response({"detail": "Your account has been deleted."}, status=status.HTTP_204_NO_CONTENT)


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Each user sees only their own skills
        return Skill.objects.filter(users=self.request.user)

    def perform_create(self, serializer):
        serializer.save(users=[self.request.user])

