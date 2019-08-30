from django.db import models


class Dist(models.Model):
    From = models.CharField(max_length=100, blank=False)
    To = models.CharField(max_length=100, blank=False)
