import graphene
import graphql_jwt
from accessCeramics.works.schema import SCHEMA as WorksSchema
from accessCeramics.users.schema import SCHEMA as UsersSchema

class Query(WorksSchema.Query, UsersSchema.Query, graphene.ObjectType):
    '''The set of all possible queries.'''
    pass

class Mutation(WorksSchema.Mutation, UsersSchema.Mutation, graphene.ObjectType):
    '''The set of all possible mutations.'''
    # graphql_jwt (auth) mutations
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

SCHEMA = graphene.Schema(query=Query, mutation=Mutation)
