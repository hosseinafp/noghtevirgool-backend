from django.db import models
from utils.general_model import GeneralModel
from django.contrib.auth import get_user_model
import uuid
import os

user = get_user_model()


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return os.path.join(f"post/{instance.pk}/", filename)


class Post(GeneralModel):
    title = models.CharField(
        max_length=250
    )
    content = models.TextField(

    )
    category = models.ManyToManyField(
        "category.Category",
        related_name="posts",
        blank=True
    )
    image = models.ImageField(
        upload_to=get_file_path,
        null=True
    )
    time_to_read = models.CharField(
        max_length=30
    )
    likes = models.ManyToManyField(
        user,
        related_name="likes",
        blank=True
    )
    bookmarks = models.ManyToManyField(
        user,
        related_name="bookmarks",
        blank=True

    )
    owner = models.ForeignKey(
        user,
        related_name="posts",
        on_delete=models.CASCADE
    )
    comments = models.ManyToManyField(
        "comment.Comment",
        blank=True,
        related_name="post"
    )
