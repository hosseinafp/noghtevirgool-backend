from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from .serializers import RegisterSerializer, UserListSerializer
from utils.base_permissions import IsNotAuthenticated, AdminRequired, MyProfilePermission
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

User = get_user_model()


class RegisterUserApiView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [IsNotAuthenticated]


class UsersListApiView(ListAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, AdminRequired)
    serializer_class = UserListSerializer


class UserProfileApiView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, MyProfilePermission)
    serializer_class = UserListSerializer

    def get_object(self):
        pk = self.request.user.pk
        return get_object_or_404(User, pk=pk)
