from django.urls import path
from post.views import PostListApiView, DetailPostApiView, UpdateDestroyPostApiView, CreatePostApiView
from user.views import RegisterUserApiView, UsersListApiView, UserProfileApiView
from comment.views import CommentsListByPostApiView, CommentsListApiView, CreateNewCommentApiView, DeleteCommentApiView

urlpatterns = [

    #Post
    path('', PostListApiView.as_view()),
    path("detail/<pk>/", DetailPostApiView.as_view()),
    path("edit/<pk>/", UpdateDestroyPostApiView.as_view()),
    path("create/", CreatePostApiView.as_view()),

    #Comment
    path("comments/list/", CommentsListApiView.as_view()),

    path("detail/<pk>/comments/", CommentsListByPostApiView.as_view()),
    path("detail/<pk>/comments/add/", CreateNewCommentApiView.as_view()),
    path("detail/<pk>/comments/remove/<int:comment_id>/", DeleteCommentApiView.as_view()),


    #User
    path("users/", UsersListApiView.as_view()),
    path("user/register/", RegisterUserApiView.as_view()),
    path("user/profile/", UserProfileApiView.as_view()),


]
