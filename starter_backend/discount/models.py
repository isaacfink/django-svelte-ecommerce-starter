from string import digits
from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from uuid import uuid4

# sale model
class sale_pricing(models.Model):
	name = models.CharField(_('name to identify in backend'), max_length=100, null=True, blank=True)
	percent_off = models.IntegerField(_('percent off'), null=True, blank=True)
	sale_price = models.DecimalField(_('sale price'), null=True, blank=True, max_digits=10, decimal_places=2)
	minimum_amount_of_products = models.IntegerField(_('minimum amount of this product'), null=True, blank=True)
	minimum_order_amount = models.BigIntegerField(_('minimum order amount'), null=True, blank=True)
	expires = models.DateTimeField(_('sale expires'), null=True, blank=True)
	uuid = models.UUIDField(_('product uuid'), default=uuid4, editable=False)

	products = models.ManyToManyField('product.product', verbose_name=_('product on sale'), blank=True)

	def validate_sale(self, order, product):

		if order.products.filter(product__uuid == self.uuid).amount < self.minimum_amount_of_products:
			return {
				'valid': False,
				'err_code': 'not enough products'
			}

		if order.amount_charged < self.minimum_order_amount:
			return {
				'valid': False,
				'err_code': 'less than minimum amount'
			}

		if self.percent_off:
			return product.product.price * self.percent_off
		else:
			return self.sale_price


	def is_expired(self):
		return self.expires < datetime.now()

# coupon model
class coupon(models.Model):
	name = models.CharField(_('name to identify in backend'), max_length=100, null=True, blank=True)
	code = models.CharField(_('coupon code'), max_length=36)
	expires = models.DateTimeField(_('coupon expiration date'), null=True, blank=True)
	maximum_uses = models.BigIntegerField(_('maximum allowed uses for this code'), null=True, blank=True)
	per_user = models.IntegerField(_('uses per customer'), null=True, blank=True)

	uses = models.BigIntegerField(_('uses so far'), default=0)

	products = models.ManyToManyField('product.product', verbose_name=_('products for this coupon'), blank=True) 

	def validate_coupon(self, order):

		# check if coupon exists for this product
		if self.products.all().length < 1:
			if self.isExpired():
				return {
					'valid': False,
					'err_code': 'coupon expired'
				}

			if (self.maximum_uses or 5) < self.uses:
				return {
					'valid': False,
					'err_code': 'maximum uses exceeded'
				}

			from order.models import order
			if self.user_exceeded_limit(order):
				return {
					'valid': False,
					'err_code': 'user exceeded coupon limit'
				}

	def is_expired(self):
		return self.expires < datetime.now()

	def user_exceeded_limit(self, current_order):
		from order.models import order
		total_used = 0
		for o in order.objects.filter(customer=current_order.customer):
			if self in o.coupons_used:
				total_used += 1

		return total_used >= self.per_user

