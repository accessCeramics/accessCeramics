import graphene
import works.schema
import users.schema

class Query(works.schema.Query, users.schema.Query, graphene.ObjectType):
    pass

class Mutation(works.schema.Mutation, users.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
