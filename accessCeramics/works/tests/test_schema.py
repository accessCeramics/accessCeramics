from django.test import TestCase
from graphene.test import Client
import schema

class MutationTests(TestCase):

    def test_create_work(self):
        '''
