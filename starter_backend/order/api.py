from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import *

class orderType(DjangoObjectType):
    class Meta:
        model = order
        filter_fields = {
            'uuid': ['exact'],
            'customer': ['exact'],
            'status': ['exact'],
            'products': ['exact', 'icontains'],
            'amount_charged': ['exact', 'lt', 'lte', 'gt', 'gte'],
            'shipping_address': ['exact'],
            "shipping": ['exact'],
            'placed_on': ['exact', 'lt', 'lte', 'gt', 'gte'],
        }

        interfaces = (relay.Node, )

class query(ObjectType):
    order = relay.node.Field(orderType)
    all_orders = DjangoFilterConnectionField(orderType)
