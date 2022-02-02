from django.urls import path
from . import api

urlpatterns = [
	# product urls
	path('products-all', api.products_all, name='products-all'),
	path('products-filter-by-tag', api.products_filter_by_tag, name='products-filter-by-tag'),
	path('products-filter-by-category', api.products_filter_by_category, name='products-filter-by-category')
]