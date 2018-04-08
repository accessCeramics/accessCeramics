import graphene
import graphql_jwt
import works.schema
import users.schema

class Query(works.schema.Query, users.schema.Query, graphene.ObjectType):
    '''The set of all possible queries.'''
    pass

class Mutation(works.schema.Mutation, users.schema.Mutation, graphene.ObjectType):
    '''The set of all possible mutations.'''
    # graphql_jwt (auth) mutations
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
