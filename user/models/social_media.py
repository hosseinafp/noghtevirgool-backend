from django.db import models
from utils.general_model import GeneralModel


class Media(GeneralModel):
    SOCIAL_CHOICES = (
        ("te", "telegram"),
        ("gi", "github"),
        ("in", "instagram"),
        ("we", "website")
    )
    title = models.CharField(
        max_length=250
    )
    url = models.URLField(
    )
    type = models.CharField(
        max_length=2,
        choices=SOCIAL_CHOICES
    )



