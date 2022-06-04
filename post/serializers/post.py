from rest_framework import serializers
from post.models import Post
from user.serializers import UserListSerializer


class PostSerializer(serializers.ModelSerializer):
    owner = UserListSerializer(read_only=True)
    class Meta:
        model = Post
        fields = "__all__"
        depth = 1