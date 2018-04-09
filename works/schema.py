import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

from users.schema import User

from .models import Work as WorkModel


class Work(DjangoObjectType):
    '''A creative work exhibited in accessCeramics.'''
    class Meta:
        model = WorkModel

class CreateWork(graphene.Mutation):
    '''Add a new work to accessCeramics.'''
    work = graphene.Field(Work)

    class Arguments:
        '''Work metadata expected from the client on creation.'''
        title = graphene.String(required=True)
        description = graphene.String()
        creators = graphene.List(graphene.Int)

    def mutate(self, info, title, description=None, creators=None):
        '''Create the work and return its information.'''
        work = WorkModel(
            title=title,
            description=description
        )
        work.save()
        # if a list of user ids was passed, those users will be creators
        if creators:
            users = [get_user_model().objects.get(pk=id) for id in creators]
        # otherwise, assume the logged in user is the creator
        else:
            users = [info.context.user]
        for user in users:
            work.creators.add(user)
        return CreateWork(work=work)

class Mutation(graphene.ObjectType):
    '''Contains functions for altering works in the database.'''
    create_work = CreateWork.Field()

class Query(graphene.ObjectType):
    '''Contains resolvers for work-related information.'''
    works = graphene.List(Work)

    def resolve_works(self, info, **kwargs):
        '''Retrieve all works in the database.'''
        return WorkModel.objects.all()
