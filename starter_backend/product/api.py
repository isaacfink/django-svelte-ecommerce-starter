from graphene import relay, ObjectType, List
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import *

class productType(DjangoObjectType):
	class Meta:
		model = product
		filter_fields = {
			'name': ['exact', 'icontains', 'istartswith'],
			'price': ['exact', 'lt', 'lte', 'gt', 'gte'],
			'category__name': ['exact', 'icontains', 'istartswith'],
			'id': ['exact'],
			'published':['exact']
		}

		interfaces = (relay.Node, )

class productOptionType(DjangoObjectType):
	class Meta:
		model = product_option
		filter_fields = {
			'name': ['exact', 'icontains', 'istartswith'],
			'price': ['exact', 'lt', 'lte', 'gt', 'gte'],
			'product__name': ['exact', 'icontains', 'istartswith'],
			'id': ['exact'],
		}

		interfaces = (relay.Node, )

class productCategoryType(DjangoObjectType):
	class Meta:
		model = product_category
		filter_fields = {
			'name': ['exact', 'icontains', 'istartswith'],
			'id': ['exact'],
		}

		interfaces = (relay.Node, )

class query(ObjectType):
	products = List(productType)
	all_products = DjangoFilterConnectionField(productType)

	product_options = relay.node.Field(productOptionType)
	all_product_options = DjangoFilterConnectionField(productOptionType)

	product_categories = relay.node.Field(productCategoryType)
	all_product_categories = DjangoFilterConnectionField(productCategoryType)

	def resolve_products(self, item):
		return product.objects.filter(published=True)
	