from django.db import models
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    '''A person involved in accessCeramics.'''
    #: first or given name, maximum 100 characters, required
    given_name = models.CharField(max_length=100,
                                  help_text=_('100 characters maximum.'))
    #: last or family name, maximum 100 characters, required
    family_name = models.CharField(max_length=100,
                                   help_text=_('100 characters maximum.'))
    #: middle or additional name
    additional_name = models.CharField(max_length=100, null=True, blank=True,
                                       help_text=_('100 characters maximum.'))
    #: birth year in YYYY format
    birth_year = models.PositiveSmallIntegerField(null=True, blank=True,
                                                  help_text=_('YYYY format.'))
    #: death year in YYYY format
    death_year = models.PositiveSmallIntegerField(null=True, blank=True,
                                                  help_text=_('YYYY format.'))

    def __str__(self):
        #: joins :attr:`given_name` with :attr:`family_name` to form full name
        return '%s %s' % (self.given_name, self.family_name)


class Artist(Person):
    '''A ceramic artist whose work is exhibited in accessCeramics.'''
    #: a statement written by the artist
    statement = models.TextField(null=True, blank=True)
    #: a descriptive biography of the artist
    bio = models.TextField(null=True, blank=True)
    #: a personal website for the artist
    website = models.URLField(null=True, blank=True)
