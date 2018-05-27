from django.test import TestCase
from django.contrib.auth.models import User
from accessCeramics.works.models import Work



class TestWork(TestCase):

    def test_str(self):
        # string representation should be work's title
        work = Work(title='cups')
        assert str(work) == work.title

