import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

import django_filters



class UserNode(DjangoObjectType):
    '''A user account in accessCeramics.'''
    class Meta:
        model = get_user_model()
        interfaces = (graphene.relay.Node,)


class UserFilter(django_filters.FilterSet):
    '''Filtering options available for users.'''
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']


class Query(graphene.ObjectType):
    '''Resolvers for user-related information.'''
    # single
    me = graphene.relay.node.Field(UserNode)
    user = graphene.relay.node.Field(UserNode)
    # filtered set
    users = DjangoFilterConnectionField(UserNode, filterset_class=UserFilter)

    @staticmethod
    def resolve_me(executor, info):
        '''Retrieve information about the current (logged-in) user.'''
        user = info.context.user
        if user.is_anonymous:
            raise Exception('User not logged in.')
        return user


class CreateUser(graphene.relay.ClientIDMutation):
    '''Register a new accessCeramics user account.'''
    user = graphene.Field(UserNode)

    class Input:
        '''User data provided by the client on registration.'''
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        first_name = graphene.String()
        last_name = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        '''Register the user and return their information.'''
        user = get_user_model()(
            username=input['username'],
            email=input['email'],
            first_name=input['first_name'],
            last_name=input['last_name']
        )
        user.set_password(input['password'])
        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    '''Contains functions for altering users in the database.'''
    create_user = CreateUser.Field()
