from django.contrib.auth import get_user_model
from django.test import TestCase
from graphene.test import Client

from accessCeramics.works.models import Technique, Material, WorkType
from accessCeramics.works.schema import SCHEMA


class TestCreateWork(TestCase):

    def setUp(self):
        # create some models to use later
        get_user_model().objects.create(
            username='budak',
            password='password'
        )
        Technique.objects.create(name='coiling')
        Material.objects.create(name='stoneware')
        WorkType.objects.create(name='bowl')


    def test_title_required(self):
        # title is required
        client = Client(SCHEMA)
        response = client.execute('''mutation {
            createWork(input: {
                date: 1990
            }) {
                work
            }
        }''')
        assert 'errors' in response
        assert 'In field \"title\"' in response['errors'][0]['message']

    def test_date_required(self):
        # date is required
        client = Client(SCHEMA)
        response = client.execute('''mutation {
            createWork(input: {
                title: "foo work"
            }) {
                work
            }
        }''')
        assert 'errors' in response
        assert 'In field \"date\"' in response['errors'][0]['message']

    def test_creator_required(self):
        # creator username is required
        client = Client(SCHEMA)
        response = client.execute('''mutation {
            createWork(input: {
                title: "foo work",
                date: 1990
            }) {
                work {
                    id
                }
            }
        }''')
        assert 'errors' in response
        assert 'username is required' in response['errors'][0]['message']

    def test_creators_exist(self):
        # specified creators must exist
        client = Client(SCHEMA)
        response = client.execute('''mutation {
            createWork(input: {
                title: "foo work",
                date: 1990,
                creators: [
                    "budak",
                    "carmen_sandiego"
                ]
            }) {
                work {
                    id
                }
            }
        }''')
        assert 'errors' in response
        assert 'carmen_sandiego does not exist' in response['errors'][0]['message']

    def test_techniques_exist(self):
        # specified techniques must exist
        client = Client(SCHEMA)
        response = client.execute('''mutation {
            createWork(input: {
                title: "foo work",
                date: 1990,
                creators: [
                    "budak"
                ]
                techniques: [
                    "basketweaving",
                    "coiling"
                ]
            }) {
                work {
                    id
                }
            }
        }''')
        assert 'errors' in response
        assert 'basketweaving does not exist' in response['errors'][0]['message']

    def test_work_types_exist(self):
        # specified work types must exist
        client = Client(SCHEMA)
        response = client.execute('''mutation {
            createWork(input: {
                title: "foo work",
                date: 1990,
                creators: [
                    "budak"
                ]
                workTypes: [
                    "bowl",
                    "plate"
                ]
            }) {
                work {
                    id
                }
            }
        }''')
        assert 'errors' in response
        assert 'plate does not exist' in response['errors'][0]['message']

    def test_materials_exist(self):
        # specified materials must exist
        client = Client(SCHEMA)
        response = client.execute('''mutation {
            createWork(input: {
                title: "foo work",
                date: 1990,
                creators: [
                    "budak"
                ]
                materials: [
                    "stoneware",
                    "rattan"
                ]
            }) {
                work {
                    id
                }
            }
        }''')
        assert 'errors' in response
        assert 'rattan does not exist' in response['errors'][0]['message']        

    def test_create_work(self):
        # create a work with correct metadata
        client = Client(SCHEMA)
        response = client.execute('''mutation {
            createWork(input: {
                title: "foo work",
                date: 1990,
                description: "A testing work",
                credits: "made by budak",
                creators: ["budak"],
                workTypes: ["bowl"],
                techniques: ["coiling"],
                materials: ["stoneware"]
            }) {
                work {
                    title
                    date
                    description
                    credits
                    creators {
                        edges {
                            node {
                                username
                            }
                        }
                    }
                    workTypes {
                        edges {
                            node {
                                name
                            }
                        }
                    }
                    techniques {
                        edges {
                            node {
                                name
                            }
                        }
                    }
                    materials {
                        edges {
                            node {
                                name
                            }
                        }
                    }
                }
            }
        }''')
        # should succeed
        assert 'errors' not in response
        assert 'data' in response
        # check metadata is the same as we passed in
        work = response['data']['createWork']['work']
        assert work['title'] == 'foo work'
        assert work['date'] == 1990
        assert work['description'] == 'A testing work'
        assert work['credits'] == 'made by budak'
        assert work['creators']['edges'][0]['node']['username'] == 'budak'
        assert work['workTypes']['edges'][0]['node']['name'] == 'bowl'
        assert work['techniques']['edges'][0]['node']['name'] == 'coiling'
        assert work['materials']['edges'][0]['node']['name'] == 'stoneware'