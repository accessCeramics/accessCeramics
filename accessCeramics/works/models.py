from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_measurement.models import MeasurementField
from measurement.measures import Distance, Temperature


class Work(models.Model):
    '''A creative work exhibited in accessCeramics.'''
    #: list of available units for height/width/depth measurements
    DISTANCE_UNITS = (
        ('m', 'm'),
        ('cm', 'cm'),
        ('in', 'in'),
        ('ft', 'ft')
    )
    #: list of available units for temperature measurements
    TEMP_UNITS = (
        ('c', 'c'),
        ('f', 'f')
    )
    #: title of the work, maximum 500 characters, required
    title = models.CharField(max_length=500,
                             help_text=_('500 characters maximum.'))
    #: usernames of accessCeramics users who created the work, required
    creators = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        help_text=_('Must be an extant accessCeramics user.'))
    #: date associated with the work, YYYY format, required
    date = models.PositiveSmallIntegerField(help_text=_('YYYY format.'))
    #: timestamp when work was created in the database
    created_at = models.DateTimeField(auto_now_add=True)
    #: timestamp when work was last modified in the database
    modified_at = models.DateTimeField(auto_now=True)
    #: description of the work or artist's statement
    description = models.TextField(
        null=True, blank=True,
        help_text=_('A description of the work or artist\'s statement.'))
    #: one or many :class:`Technique` used to make the work
    techniques = models.ManyToManyField('Technique', blank=True)
    #: one or many :class:`Material` used to make the work
    materials = models.ManyToManyField('Material', blank=True)
    #: one or many :class:`WorkType` describing the work
    work_types = models.ManyToManyField('WorkType', blank=True)
    #: one or many :class:`PyrometricCone` used to fire the work
    pyrometric_cones = models.ManyToManyField('PyrometricCone', blank=True)
    #: a :class:`measurement.measures.Temperature` at which the work was fired
    firing_temperature = MeasurementField(measurement=Temperature, null=True,
                                          blank=True, unit_choices=TEMP_UNITS)
    #: a :class:`measurement.measures.Temperature` of a second firing, if any
    second_firing_temperature = MeasurementField(measurement=Temperature,
                                                 null=True, blank=True,
                                                 unit_choices=TEMP_UNITS)
    #: a :class:`measurement.measures.Distance` for the height of the work
    height = MeasurementField(measurement=Distance, null=True, blank=True,
                              unit_choices=DISTANCE_UNITS)
    #: a :class:`measurement.measures.Distance` for the width of the work
    width = MeasurementField(measurement=Distance, null=True, blank=True,
                             unit_choices=DISTANCE_UNITS)
    #: a :class:`measurement.measures.Distance` for the depth of the work
    depth = MeasurementField(measurement=Distance, null=True, blank=True,
                             unit_choices=DISTANCE_UNITS)

    def __str__(self):
        #: default string representation. uses :attr:`title`.
        return self.title


class Technique(models.Model):
    '''An artistic technique used in the making of a work.'''
    #: name of the technique - max 100 characters
    name = models.CharField(max_length=100)

    def __str__(self):
        #: default string representation. uses :attr:`name`
        return self.name


class Material(models.Model):
    '''A material used to make a work.'''
    #: name of the material - max 100 characters
    name = models.CharField(max_length=100)

    def __str__(self):
        #: default string representation. uses :attr:`name`
        return self.name


class WorkType(models.Model):
    '''The type or function of a work, e.g. "vase".'''
    #: name of the work type - max 100 characters
    name = models.CharField(max_length=100)

    def __str__(self):
        #: default string representation. uses :attr:`name`
        return self.name


class PyrometricCone(models.Model):
    '''A pyrometric cone used to fire a ceramic work.'''
    #: cone number - max 4 characters
    number = models.CharField(max_length=4)

    def __str__(self):
        #: default string representation. uses :attr:`number`
        return self.number
