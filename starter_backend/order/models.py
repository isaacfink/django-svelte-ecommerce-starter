from django.db import models
from django.utils.translation import gettext_lazy as _
from uuid import uuid4

# order model
class order(models.Model):
	uuid = models.UUIDField(_('uuid field'), default=uuid4(), unique=True, help_text='uuid field gives each order a unique identifier')
	customer = models.ForeignKey('users.customer', verbose_name=_('order cutomer'), help_text='customer who placed this order', on_delete=models.SET_NULL, null=True, blank=True)

	placed_on = models.DateTimeField(_('placed on'), auto_now_add=True, help_text='when this order was placed')

	draft = models.BooleanField(_('order is a draft'), default=False)

	# shipping info
	shipping = models.BooleanField(_('shipping'), default=False)
	shipping_address = models.ForeignKey('users.address', null=True, blank=True, verbose_name=_('shipping address'), on_delete=models.SET_NULL)

	# payment info
	amount_charged = models.BigIntegerField(_('amount charged'), help_text=('amount for charged for order'))
	pre_tax_amount = models.BigIntegerField(_('pre tax amount'), help_text='order total before tax', null=True, blank=True)
	tax_amount = models.BigIntegerField(_('taxes charged'), help_text='amount charged for taxes', default=0)
	shipping_amount = models.BigIntegerField(_('shipping charged'), help_text='amount charged for shipping', default=0)

	# order info
	products = models.ManyToManyField('product.configured_product', verbose_name=_('products in order'))
	gift = models.BooleanField(_('gift'), default=False, help_text='is this order a gift')
	gift_from = models.CharField(_('gift from'), max_length=250, help_text='who is this gift from', null=True, blank=True)
	gift_to = models.CharField(_('gift to'), max_length=250, help_text='who is this gift for', null=True, blank=True)
	gift_message = models.CharField(_('gift message'), max_length=250, help_text='message for gift', null=True, blank=True)

	# discounts info
	coupons_used = models.ManyToManyField('discount.coupon', verbose_name=_('coupons used on this order'), blank=True)

	# status
	STATUS_CHOICES = (
			('draft', 'draft'),
			('paid', 'paid'),
			('processing', 'processing'),
			('shipped', 'shipped'),
			('in transit', 'in transit'),
			('delivered', 'delivered'),
			('picked up', 'picked up'),
			('error', 'error')
		)
	status = models.CharField(_('order status'), choices=STATUS_CHOICES, default='paid', max_length=50)

	def amount_of_products(self):
		return self.products.all().count()

# wish list model
class wish_list(models.Model):
	customer = models.ForeignKey('users.customer', verbose_name=_('customer'), on_delete=models.CASCADE)
	name = models.CharField(_('name'), default='wish list', max_length=100)
	get_notifications = models.BooleanField(_('get notifications'), default=False)

	products = models.ManyToManyField('product.configured_product', verbose_name=_('products in wish list'), blank=True)
