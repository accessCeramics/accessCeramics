from django.db import models
from django.conf import settings

class Work(models.Model):
    '''A creative work exhibited in accessCeramics.'''
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    creators = models.ManyToManyField(settings.AUTH_USER_MODEL)
