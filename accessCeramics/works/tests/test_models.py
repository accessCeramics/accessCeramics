from django.contrib.auth.models import User
from django.test import TestCase
from measurement.measures import Distance, Temperature

from accessCeramics.works.models import (Material, PyrometricCone, Technique,
                                         Work, WorkType)


class TestWork(TestCase):

    def test_str(self):
        # string representation should be work title
        work = Work(title='cups')
        assert str(work) == work.title


class TestTechnique(TestCase):

    def test_str(self):
        # string representation should be technique name
        technique = Technique(name='throwing')
        assert str(technique) == technique.name


class TestMaterial(TestCase):

    def test_str(self):
        # string representation should be material name
        material = Material(name='stoneware')
        assert str(material) == material.name


class TestWorkType(TestCase):

    def test_str(self):
        # string representation should be work type name
        work_type = WorkType(name='sculpture')
        assert str(work_type) == work_type.name


class TestPyrometricCone(TestCase):

    def test_str(self):
        # string representation should be cone number
        cone = PyrometricCone(number='022')
        assert str(cone) == cone.number
