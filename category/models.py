from django.db import models
from utils.general_model import GeneralModel


class Category(GeneralModel):
    name = models.CharField(
        max_length=250
    )