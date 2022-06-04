from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import os


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return os.path.join(f"user/{instance.pk}/", filename)



class User(AbstractUser):
    email = models.EmailField(
        unique=True
    )
    is_admin = models.BooleanField(
        default=False
    )
    position = models.CharField(
        max_length=200,
        null=True
    )
    image = models.ImageField(
        upload_to=get_file_path,
        default="user_default.jpg"
    )
    skills = models.ManyToManyField(
        "user.Skill",
        blank=True
    )
    social_media = models.ManyToManyField(
        "user.Media",
        blank=True,
        related_name="owner"
    )


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
