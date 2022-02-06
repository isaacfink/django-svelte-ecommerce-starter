from django.db import models
from django.utils.translation import gettext_lazy as _

# payment method model
class method(models.Model):

	METHOD_CHOICES = (
			('cc', 'cc'),
			('google pay', 'google pay'),
			('apple pay', 'apple pay'),
			('paypal', 'paypal')
		)

	method = models.CharField(_('payment method'), choices=METHOD_CHOICES, max_length=50)
	token = models.CharField(_('payment token'), max_length=512)
