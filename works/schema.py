import graphene
from graphene_django import DjangoObjectType

from .models import Work as WorkModel


class Work(DjangoObjectType):
    '''A creative work exhibited in accessCeramics.'''
    class Meta:
        model = WorkModel

class CreateWork(graphene.Mutation):
    '''Add a new work to accessCeramics.'''
    id = graphene.Int()
    title = graphene.String()
    description = graphene.String()

    class Arguments:
        '''Properties available when creating a work.'''
        title = graphene.String()
        description = graphene.String()

    def mutate(self, info, title, description):
        '''Create the work and return its information.'''
        work = WorkModel(title=title, description=description)
        work.save()

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
