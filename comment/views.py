from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated
from utils.base_permissions import AdminRequired
from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse
from post.models import Post


class CommentsListApiView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, AdminRequired)


class CommentsListByPostApiView(ListAPIView):
    serializer_class = CommentSerializer
    lookup_field = "post__pk"

    def get_queryset(self):
        post_pk = self.kwargs["pk"]
        return Comment.objects.filter(post__pk=post_pk)


class CreateNewCommentApiView(CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        received_data = request.POST
        post = kwargs["pk"]
        post = get_object_or_404(Post, pk=post)
        content = received_data["content"]
        user = request.user
        parent = received_data["parent"] if received_data["parent"] != "" else None
        if parent:
            parent = get_object_or_404(Comment, id=int(parent)) or None

        comment = Comment.objects.create(
            content=content,
            parent=parent,
            sender = user
        )
        comment.save()
        post.comments.add(comment)
        comment = CommentSerializer(comment)

        return JsonResponse(
            status=201,
            data=comment.data
        )


class DeleteCommentApiView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, AdminRequired)

    def delete(self, request, *args, **kwargs):
        user = request.user
        comment = get_object_or_404(Comment, pk=kwargs['comment_id'])
        comment.delete()
        return JsonResponse(
            status=204,
            data={
                "msg": "No Content"
            }
        )

