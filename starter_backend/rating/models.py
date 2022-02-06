from django.db import models
from django.utils.translation import gettext_lazy as _

# rating model
class rating(models.Model):
	rating = models.IntegerField(_('user rating'))
	customer = models.OneToOneField('users.customer', verbose_name=_('rating owner'), on_delete=models.SET_NULL, null=True, blank=True)
	product = models.ForeignKey('product.product', verbose_name=_('rated product'), on_delete=models.SET_NULL, null=True, blank=True)

	review = models.TextField(_('customer review'), null=True, blank=True)
	customer_images = models.ManyToManyField('rating.image', verbose_name=_('customer images'), blank=True)

	def validate_rating(self):
		for o in self.customer.order.filter(customer=self.customer):
			if self.product in o.products and o.status in ['delivered', 'picked up']:
				return True

		return False

# customer images model
class image(models.Model):
	image = models.ImageField(_('customer image'), upload_to='product-images/customer-uploaded')