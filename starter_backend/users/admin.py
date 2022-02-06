from django.contrib import admin
from .models import (
    customer,
    User,
    address
)

# Register your models here.
admin.site.register(customer)
admin.site.register(User)
admin.site.register(address)
