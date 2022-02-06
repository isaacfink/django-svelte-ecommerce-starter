from product.models import (
		product,
		product_package,
		product_category
	)

def calculate_total_price(order):
	total_price = 0
	for p in order.products.all():
		total_price += p.option.price

	return total_price

def calculate_taxes(order):
	pass

def calculate_total_with_coupons(order):
	pass
