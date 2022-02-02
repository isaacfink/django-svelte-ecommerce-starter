from .models import (
		product,
		product_category,
		product_package,tag

	)

# products views
def products_all(request):
	pass

def products_filter_by_tag(request):
	query = product.objects.filter(tag = tag.objects.get(name=request.GET.get('tag')))

def products_filter_by_category(request):
	query = product.objects.filter(category=category.objects.get(name=request.GET.get('category')))

	