'''
This script will load a JSON-format file containing accessCeramics records
into the database. It expects the file to contain an array of objects with
keys corresponding to the field names of the Work model. Multivalued fields
should be represented as arrays of strings. Measurement fields should be
represented as floating point values in inches. Empty fields should use the
JSON value `none`.
'''

import json

from django.core.management.base import BaseCommand
from measurement.measures import Distance

from accessCeramics.works.models import Material, Technique, Work, WorkType


class Command(BaseCommand):

    def add_arguments(self, parser):
        '''Command takes one argument - the path to the JSON file to import.'''
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        '''Called when the user executes the command. In this case, it would be:
        `python manage.py import_works path/to/file.json`'''

        with open(options['path'], 'r') as json_file:
            json_string = json_file.read()
        work_list = json.loads(json_string)

        for entry in work_list:
            work = Work()
            # basic metadata
            work.title = entry['title']
            work.date = int(entry['date'])
            # dimensions
            if entry['height']:
                work.height = Distance(inch=float(entry['height']))
            if entry['width']:
                work.width = Distance(inch=float(entry['width']))
            if entry['depth']:
                work.depth = Distance(inch=float(entry['depth']))
            # tags
            work.save()
            for technique_name in entry['techniques']:
                technique, _ = Technique.objects.get_or_create(name=technique_name)
                work.techniques.add(technique)
            for material_name in entry['materials']:
                material, _ = Material.objects.get_or_create(name=material_name)
                work.materials.add(material)
            for work_type_name in entry['work_types']:
                work_type, _ = WorkType.objects.get_or_create(name=work_type_name)
                work.work_types.add(work_type)
