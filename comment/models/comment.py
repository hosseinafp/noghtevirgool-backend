from django.db import models
from utils.general_model import GeneralModel
from django.contrib.auth import get_user_model

user = get_user_model()


class Comment(GeneralModel):
    content = models.TextField(

    )
    parent = models.ForeignKey(
        "self",
        related_name="owner",
        null=True,
        on_delete=models.CASCADE
    )
    sender = models.ForeignKey(
        user,
        related_name="comments",
        on_delete=models.CASCADE
    )
