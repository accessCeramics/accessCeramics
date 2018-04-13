from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Work(models.Model):
    '''A creative work exhibited in accessCeramics.'''
    title = models.CharField(_('title'), max_length=500, help_text=_('The title of the work. Max 500 characters.'))
    description = models.TextField(_('description'), null=True, help_text=_('A short description of the work.'))
    creators = models.ManyToManyField(settings.AUTH_USER_MODEL, help_text=_('accessCeramics user(s) who created the work.'))
    techniques = models.ManyToManyField('Technique', help_text=_('Artistic techniques used to make the work.'))
    materials = models.ManyToManyField('Material', help_text=_('Materials used to make the work.'))
    work_types = models.ManyToManyField('WorkType', help_text=_('Types or functions of the work, e.g. "vase".'))

    def __str__(self):
        return self.title


class Technique(models.Model):
    '''An artistic technique used in the making of a work.'''
    name = models.CharField(max_length=100, help_text=_('An artistic technique used in the making of a work.'))

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


# class Temperature(models.Model):
    # '''A measurement of heat used in the making of a work.'''
    # value = models.IntegerField()
    # CONE_VALUES = {
    #     '022': 600,
    #     '021': 614,
    #     '020': 635,
    #     '019': 683,
    #     '018': 717,
    #     '017': 747,
    #     '016': 792,
    #     '015': 804,
    #     '014': 838,
    #     '013': 852,
    #     '012': 884,
    #     '011': 894,
    #     '010': 900,
    #     '09': 923,
    #     '08': 955,
    #     '07': 984,
    #     '06': 999,
    #     '05': 1046,
    #     '04': 1060,
    #     '03½': 1080,
    #     '03': 1101,
    #     '02': 1120,
    #     '01': 1137,
    #     '1': 1154,
    #     '2': 1162,
    #     '3': 1168,
    #     '4': 1186,
    #     '5': 1196,
    #     '6': 1222,
    #     '7': 1240,
    #     '8': 1263,
    #     '9': 1280,
    #     '10': 1305,
    #     '11': 1315,
    #     '12': 1326,
    #     '13': 1246
    # }

    # def to_cone(self):
    #     '''use list bisection to find the closest matching cone value.'''
    #     temps = self.CONE_VALUES.keys()
    #     index = bisect_left(temps, self.value)
    #     if index == 0:
    #         return (temps[0], 'Cone')
    #     if index == len(temps):
    #         return (temps[-1], 'Cone')
    #     before = temps[index-1]
    #     after = temps[index]
    #     if after - self.value < self.value - before:
    #         return (after, 'Cone')
    #     return (before, 'Cone')

    # def to_fahrenheit(self):
    #     '''convert celsius to fahrenheit and return with unit.'''
    #     return (self.value * (9/5) + 32, '°F')

    # def to_celsius(self):
    #     '''return celsius and unit.'''
    #     return (self.value, '°C')

    # def __str__(self):
    #     return self.to_celsius()
    