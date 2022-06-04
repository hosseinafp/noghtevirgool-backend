from rest_framework import serializers
from comment.models import Comment
from user.serializers import UserListSerializer


class CommentSerializer(serializers.ModelSerializer):
    sender = UserListSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"