import random

from django.db import models
from django.db.models import JSONField


class Route(models.Model):
    name = models.CharField(max_length=256)
    data = JSONField(null=True, blank=True)
    center_coordinates = JSONField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    SAMPLE_IMAGES = [
        "/samples/Anthering.jpg",
        "/samples/Georgenberg.jpg",
        "/samples/Postalm.jpg",
        "/samples/Schafberg.jpg",
    ]

    def __str__(self):
        return self.name

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.image:
            self.image = random.choice(self.SAMPLE_IMAGES)

        return super().save(force_insert, force_update, using, update_fields)
