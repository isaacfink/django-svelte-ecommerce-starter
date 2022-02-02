from django.db import models
from django.utils.translation import gettext_lazy as _
from rating.models import rating

# product model
class product(models.Model):
	# general info
	name = models.CharField(_('product name'), max_length='100')
	slug = models.SlugField(_('product slug'))
	description = models.TextField(_('product description'))
	price = models.DecimalField(_('product price'), decimal_places=2, max_digits=2)
	main_image = models.ImageField(_('main product image'), upload_to='product-images/')
	secondary_images = models.ManyToManyField('product.image', verbose_name=_('product secondary images'))

	physical_item = models.BooleanField(_('is item physical'), default=True)
	in_stock = models.BigIntegerField(_('products in stock'), default=0)

	# seo info
	seo_name = models.CharField(_('seo name'), max_length=250)
	seo_description = models.TextField(_('seo description'))

	# aditional fields info
	separate_options_price = models.BooleanField(_('options are priced separately'), default=False, help_text='if checked this will give each option an individual price, otherwise the options will inherit the price from the product')
	options = models.ManyToManyField('product.product_option', verbose_name=_('product options'))
	tags = models.ManyToManyField('product.tag')
	category = models.ForeignKey('product.product_category', verbose_name=_('product category'), on_delete=models.SET_NULL, null=True, blank=True)

	def lowest_price(self):
		if self.separate_options_price:
			return self.options.all(order_by='price').first().price
		else:
			return self.price

	def highest_price(self):
		if self.separate_options_price:
			return self.options.all(order_by='price').first().price
		else:
			return self.price

	def get_rating(self):
		count = 0
		rating = 0
		for r in rating.objects.filter(product=self):
			rating += r.ratings
			count += 1
			
		return rating / count

# package model
class product_package(models.Model):
	name = models.CharField(_('package name'), max_length=100)
	price = models.DecimalField(_('package price'), decimal_places=2, default=0, max_digits=2)

	products = models.ManyToManyField('product.product', verbose_name='package products')

	def get_amount_of_products(self):
		return self.products.all().count

# category model
class product_category(models.Model):
	name = models.CharField(_('category name'), max_length=200)
	description = models.TextField(_('category description'))
	main_image = models.ImageField(_('category image'), upload_to='category-images')

	def get_all_products(self):
		return product.objects.get(category=self)

	def get_amount_of_products(self):
		return product.objects.get(category=self).count()

# product options model
class product_option(models.Model):
	name = models.CharField(_('option name'), max_length=100)
	main_image = models.ImageField(_('main product image'), upload_to='product-images/options')
	secondary_images = models.ManyToManyField('product.image', verbose_name=_('product secondary images'))
	price = models.DecimalField(_('option price'), decimal_places=2, help_text='if left empty price will be same as product', default=0, max_digits=2)

	physical_item = models.BooleanField(_('is item physical'), default=True)
	in_stock = models.BigIntegerField(_('in stock'), default=0)

# configured product model
class configured_product(models.Model):
	product = models.ForeignKey('product.product', verbose_name=_('product'), on_delete=models.CASCADE)
	option = models.ForeignKey('product.product_option', verbose_name=_('chosen option'), on_delete=models.CASCADE),
	amount = models.BigIntegerField(_('amount'))

# tag model
class tag(models.Model):
	name = models.CharField(_('tag name'), max_length=50)
	color = models.CharField(_('tag color'), default='#ffffff', max_length=7)
	text_color_dark = models.BooleanField(_('dark text'), default=True)

	def get_all_products(self):
		return product.objects.filter(tag__contains=self)

	def get_amount_of_products(self):
		return product.objects.filter(tag__contains=self).count()


# product secondary images model
class image(models.Model):
	image = models.ImageField(_('secondary product image'), upload_to='product-images/secondary')
