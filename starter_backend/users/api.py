from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import *

class customerType(DjangoObjectType):
	class Meta:
		model = customer
		filter_fields = {
			'uuid': ['exact'],
			'first_name': ['exact', 'icontains', 'istartswith'],
			'last_name': ['exact', 'icontains', 'istartswith'],
			'email_address': ['exact', 'icontains', 'istartswith'],
			'phone_number': ['exact', 'icontains', 'istartswith'],
			'id': ['exact'],
		}

		interfaces = (relay.Node, )

class query(ObjectType):
	customer = relay.node.Field(customerType)
	all_customers = DjangoFilterConnectionField(customerType)