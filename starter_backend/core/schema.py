from graphene import ObjectType, Schema
from graphene_django import DjangoObjectType
from product.api import query as product_query
from order.api import query as order_query
from users.api import query as user_query

class query(product_query, user_query, order_query, ObjectType):
    pass

schema = Schema(query=query)