from django.db import models

class Work(models.Model):
    '''A creative work exhibited in accessCeramics.'''
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True)
