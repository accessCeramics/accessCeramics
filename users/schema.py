import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType


class User(DjangoObjectType):
    '''A user account in accessCeramics.'''
    class Meta:
        model = get_user_model()

class CreateUser(graphene.Mutation):
    '''Register a new accessCeramics user account.'''
    user = graphene.Field(User)

    class Arguments:
        '''User data expected from the client on registration.'''
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        first_name = graphene.String()
        last_name = graphene.String()

    def mutate(self, info, username, password, email, first_name=None, last_name=None):
        '''Register the user and return their information.'''
        user = get_user_model()(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)

class Mutation(graphene.ObjectType):
    '''Contains functions for altering users in the database.'''
    create_user = CreateUser.Field()

class Query(graphene.ObjectType):
    '''Contains resolvers for user-related information.'''
    me = graphene.Field(User)
    users = graphene.List(User)

    def resolve_me(self, info, **kwargs):
        '''Retrieve information about the current (logged-in) user.'''
        user = info.context.user
        if user.is_anonymous:
            raise Exception('User not logged in.')

        return user

    def resolve_users(self, info, **kwargs):
        '''Retrieve all users in the database.'''
        return get_user_model().objects.all()
