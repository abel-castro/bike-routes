from django.db import models
from django.db.models import JSONField


class Route(models.Model):
    name = models.CharField(max_length=256, unique=True)
    data = JSONField(null=True, blank=True)
    center_coordinates = JSONField(null=True, blank=True)

    def __str__(self):
        return self.name
