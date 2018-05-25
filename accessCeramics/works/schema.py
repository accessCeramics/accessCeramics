import django_filters
import graphene
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Material as MaterialModel
from .models import Technique as TechniqueModel
from .models import Work as WorkModel
from .models import WorkType as WorkTypeModel


class WorkNode(DjangoObjectType):
    class Meta:
        model = WorkModel
        interfaces = (graphene.relay.Node,)


class TechniqueNode(DjangoObjectType):
    class Meta:
        model = TechniqueModel
        interfaces = (graphene.relay.Node,)


class MaterialNode(DjangoObjectType):
    class Meta:
        model = MaterialModel
        interfaces = (graphene.relay.Node,)


class WorkTypeNode(DjangoObjectType):
    class Meta:
        model = WorkTypeModel
        interfaces = (graphene.relay.Node,)


class WorkFilter(django_filters.FilterSet):
    '''Filtering options available for works.'''
    class Meta:
        model = WorkModel
        fields = ['title', 'description']


class TechniqueFilter(django_filters.FilterSet):
    '''Filtering options available for techniques.'''
    class Meta:
        model = TechniqueModel
        fields = ['name']


class MaterialFilter(django_filters.FilterSet):
    '''Filtering options available for materials.'''
    class Meta:
        model = MaterialModel
        fields = ['name']


class WorkTypeFilter(django_filters.FilterSet):
    '''Filtering options available for work types.'''
    class Meta:
        model = WorkTypeModel
        fields = ['name']


class Query(graphene.ObjectType):
    '''Resolvers for work-related information.'''
    # single
    work = graphene.relay.node.Field(WorkNode)
    technique = graphene.relay.node.Field(TechniqueNode)
    material = graphene.relay.node.Field(MaterialNode)
    workType = graphene.relay.node.Field(WorkTypeNode)
    # filtered set
    works = DjangoFilterConnectionField(WorkNode, filterset_class=WorkFilter)
    techniques = DjangoFilterConnectionField(TechniqueNode, filterset_class=TechniqueFilter)
    materials = DjangoFilterConnectionField(MaterialNode, filterset_class=MaterialFilter)
    workTypes = DjangoFilterConnectionField(WorkTypeNode, filterset_class=WorkTypeFilter)


class CreateWork(graphene.relay.ClientIDMutation):
    '''Add a new work to accessCeramics.'''
    work = graphene.Field(WorkNode)

    class Input:
        '''Work metadata provided by the client on creation.'''
        # basic metadata
        title = graphene.String(
            required=True,
            description=WorkModel._meta.get_field('title').help_text)
        creators = graphene.List(
            graphene.String,
            description=WorkModel._meta.get_field('creators').help_text)
        date = graphene.Int(
            required=True,
            description=WorkModel._meta.get_field('date').help_text)
        # additional metadata
        description = graphene.String(
            description=WorkModel._meta.get_field('description').help_text)
        credits = graphene.String(
            description=WorkModel._meta.get_field('credits').help_text)
        # tags
        techniques = graphene.List(
            graphene.String,
            description=WorkModel._meta.get_field('techniques').help_text)
        materials = graphene.List(
            graphene.String,
            description=WorkModel._meta.get_field('materials').help_text)
        work_types = graphene.List(
            graphene.String,
            description=WorkModel._meta.get_field('work_types').help_text)
        # TODO implement temperature ?
        # TODO implement measurements


    @classmethod
    def mutate_and_get_payload(cls, root, info, **kwargs):
        '''Create the work and return its information.'''
        work = WorkModel(
            title=kwargs['title'],
            date=kwargs['date']
        )
        if 'description' in kwargs:
            work.description = kwargs['description']
        if 'credits' in kwargs:
            work.credits = kwargs['credits']
        work.save()

        if 'creators' in kwargs:
            # if users were specified as creators, add them
            for creator in kwargs['creators']:
                try:
                    work.creators.add(
                        get_user_model().objects.get(username=creator))
                except get_user_model().DoesNotExist:
                    raise get_user_model().DoesNotExist(
                        # raise a more useful error indicating which user failed
                        f'User matching query {creator} does not exist.')
        elif hasattr(info.context, 'user'):
            # otherwise assume the current user is the creator
            work.creators.add(info.context.user)
        else:
            # if the request was anonymous and no user supplied, raise an error
            raise ValidationError('Creator username is required.')

        if 'techniques' in kwargs:
            for technique in kwargs['techniques']:
                try:
                    work.techniques.add(
                        TechniqueModel.objects.get(name=technique))
                except TechniqueModel.DoesNotExist:
                    raise TechniqueModel.DoesNotExist(
                        f'Technique matching query {technique} does not exist.')

        if 'materials' in kwargs:
            for material in kwargs['materials']:
                try:
                    work.materials.add(
                        MaterialModel.objects.get(name=material))
                except MaterialModel.DoesNotExist:
                    raise MaterialModel.DoesNotExist(
                        f'Material matching query {material} does not exist.')

        if 'work_types' in kwargs:
            for work_type in kwargs['work_types']:
                try:
                    work.work_types.add(
                        WorkTypeModel.objects.get(name=work_type))
                except WorkTypeModel.DoesNotExist:
                    raise WorkTypeModel.DoesNotExist(
                        f'Work type matching query {work_type} does not exist.')

        return CreateWork(work=work)


class Mutation(graphene.ObjectType):
    '''Functions for altering works in the database.'''
    create_work = CreateWork.Field()

SCHEMA = graphene.Schema(query=Query, mutation=Mutation)
