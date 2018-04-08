import graphene
import works.schema

class Query(works.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
