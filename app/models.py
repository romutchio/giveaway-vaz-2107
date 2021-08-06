from django.db import models


class Slot(models.Model):
    is_free = models.BooleanField(default=True)
    username = models.CharField(max_length=100, blank=True, null=True)
