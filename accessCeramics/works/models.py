from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_measurement.models import MeasurementField
from measurement.measures import Distance
from measurement.measures import Temperature as TemperatureMeasure


class Work(models.Model):
    '''A creative work exhibited in accessCeramics.'''
    # basic metadata
    title = models.CharField(max_length=500,
                             help_text=_('500 characters maximum.'))
    creators = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        help_text=_('Must be an extant accessCeramics user.'))
    date = models.PositiveSmallIntegerField(help_text=_('Use YYYY format.'))
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    # additional metadata
    description = models.TextField(
        null=True, blank=True,
        help_text=_('A description of the work or artist\'s statement.'))
    credits = models.TextField(
        null=True, blank=True,
        help_text=_('Credit line, e.g. for photographing the work.'))
    # tags
    techniques = models.ManyToManyField('Technique', blank=True)
    materials = models.ManyToManyField('Material', blank=True)
    work_types = models.ManyToManyField('WorkType', blank=True)
    temperatures = models.ManyToManyField('Temperature', blank=True)
    # dimensions
    height = MeasurementField(measurement=Distance, null=True, blank=True)
    width = MeasurementField(measurement=Distance, null=True, blank=True)
    depth = MeasurementField(measurement=Distance, null=True, blank=True)

    def __str__(self):
        return self.title


class Technique(models.Model):
    '''An artistic technique used in the making of a work.'''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Material(models.Model):
    '''A material used to make a work.'''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class WorkType(models.Model):
    '''The type or function of a work, e.g. "vase".'''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Temperature(models.Model):
    '''Previous temperature of the work, e.g. when fired in a kiln.'''
    value = MeasurementField(measurement=TemperatureMeasure)

    CONE_VALUES = {
        '022': 600,
        '021': 614,
        '020': 635,
        '019': 683,
        '018': 717,
        '017': 747,
        '016': 792,
        '015': 804,
        '014': 838,
        '013': 852,
        '012': 884,
        '011': 894,
        '010': 900,
        '09': 923,
        '08': 955,
        '07': 984,
        '06': 999,
        '05': 1046,
        '04': 1060,
        '03½': 1080,
        '03': 1101,
        '02': 1120,
        '01': 1137,
        '1': 1154,
        '2': 1162,
        '3': 1168,
        '4': 1186,
        '5': 1196,
        '6': 1222,
        '7': 1240,
        '8': 1263,
        '9': 1280,
        '10': 1305,
        '11': 1315,
        '12': 1326,
        '13': 1246
    }

    # @property
    # def cone_value(self):
    #     '''use list bisection to find the closest matching cone value.'''
    #     cones = CONE_VALUES.keys()
    #     index = bisect_left(cones, temperature)
    #     if index == 0:
    #         return cones[0]
    #     if index == len(cones):
    #         return cones[-1]
    #     before = cones[index-1]
    #     after = cones[index]
    #     if after - temperature < temperature - before:
    #         return after
    #     return before

    def __str__(self):
        return self.value
