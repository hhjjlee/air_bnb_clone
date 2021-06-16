from django.db import models
from core import models as core_models

""" List Model Definition """


class List(core_models.TimeStampedModel):
    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    rooms = models.ManyToManyField("rooms.Room", blank=True)

# this def make topic return as i input on name field.

    def __str__(self):
        return self.name
