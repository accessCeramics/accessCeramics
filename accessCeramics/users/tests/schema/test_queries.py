from django.test import TestCase
from graphene.test import Client
from accessCeramics.users.schema import SCHEMA


class TestMe(TestCase):

    def test_login_required(self):
        # should throw an error if not logged in
        client = Client(SCHEMA)
        response = client.execute('''query {
            me {
                username
            }
        }''')
        assert 'errors' in response
        assert response['errors']
