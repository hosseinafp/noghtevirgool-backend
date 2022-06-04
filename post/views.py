from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, RetrieveAPIView
from .models import Post
from .serializers import PostSerializer
from utils.base_permissions import AdminRequired, IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated


class PostListApiView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CreatePostApiView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)


class UpdateDestroyPostApiView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, IsAdminOrReadOnly)


class DetailPostApiView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

