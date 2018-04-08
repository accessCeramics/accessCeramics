import graphene
from graphene_django import DjangoObjectType

from .models import Work as WorkModel

class Work(DjangoObjectType):
    class Meta:
        model = WorkModel

class Query(graphene.ObjectType):
    works = graphene.List(Work)

    def resolve_works(self, info, **kwargs):
        return WorkModel.objects.all()