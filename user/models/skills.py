from django.db import models
from utils.general_model import GeneralModel


class Skill(GeneralModel):
    name = models.CharField(
        max_length=250
    )
    percent = models.IntegerField(
    )



