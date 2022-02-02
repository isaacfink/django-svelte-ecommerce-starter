from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from uuid import uuid4

# Base user
class User(AbstractUser:
	username = None
	email = models.EmailField(_('email address'), unique=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	def __str__(self):
		return self.email

# customer account
class customer(models.Model):

	user = models.OneToOneField("account.User", verbose_name=_("customer user account"), on_delete=models.CASCADE)

	# general info
	first_name = models.CharField(_('customer first name'), max_length=100, help_text='customer first name')
	last_name = models.CharField(_('customer last name'), max_length=100, help_text='customer last name')

	phone_number = models.BigIntegerField(_('customer phone number'), help_text='customer phone number')

	# addresses info
	addresses = models.ManyToManyField('account.address', verbose_name=_('customer addresses'), related_name='customer_addresses')
	default_shipping_address = models.ForeignKey('account.address', verbose_name=_('default shipping address'), on_delete=models.SET_NULL, null=True, blank=True, related_name='default_shipping')
	default_billing_address = models.ForeignKey('account.address', verbose_name=_('default billing address'), help_text='default address for new payment methods', on_delete=models.SET_NULL, null=True, blank=True, related_name='default_billing')

	# payment info
	payments = models.ManyToManyField('payment.method', verbose_name=_('payment methods'), related_name='payments')
	default_payment = models.ForeignKey('payment.method', verbose_name=_('default payment'), help_text='default payment for new orders', on_delete=models.SET_NULL, null=True, blank=True, related_name='default_payment')

# address model
class address(models.Model):
	street_1 = models.CharField(_('street address 1'), max_length=250, help_text='street address one')
	street_2 = models.CharField(_('street address 2'), null=True, blank=True, max_length=250, help_text='street address two')

	postal_code = models.IntegerField(_('address zipcode'), help_text='address zipcode')
	city = models.CharField(_('address city'), max_length=100, help_text='address city')
	state = models.CharField(_('address state'), max_length=50, help_text='address state')
	country = models.CharField(_('address country'), max_length=100, help_text='address country')

	def short_address(self, street):
		return f'{street}'

	def full_address(self, street):
		return f'{street} {self.city} {self.state} {self.postal_code} {self.country}'
		

	def address_without_country(self, street):
		return f'{street} {self.city} {self.state} {self.postal_code}'

	def full_address_street_1(self):
		return self.full_address(self, self.street_1)

	def short_address_street_1(self):
		return short_address(self, self.street_1)

	def address_without_country_street_1(self):
		return self.address_without_country(self, self.street_1)

	def full_address_street_2(self):
		return self.full_address(self, self.street_2)

	def short_address_street_2(self):
		return short_address(self, self.street_2)

	def address_without_country_street_2(self):
		return self.address_without_country(self, self.street_2)



	class Meta:
		verbose_name = 'address'
		verbose_name_plural = 'adresses'

