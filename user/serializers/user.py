from django.contrib.auth import get_user_model
from rest_framework import serializers
User = get_user_model()


class UserListSerializer(serializers.ModelSerializer):
    is_admin = serializers.BooleanField(
        read_only=True
    )
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "image",
            "position",
            "is_admin",
            "skills",
            "social_media"
        ]
        depth = 1