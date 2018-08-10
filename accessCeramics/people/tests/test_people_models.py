from django.test import TestCase

from accessCeramics.people.models import Person


class TestPerson(TestCase):

    def test_str(self):
        # string representation should be given name and family name together
        person = Person(given_name='Ted', family_name='Vogel')
        assert str(person) == 'Ted Vogel'
