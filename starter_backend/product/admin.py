from django.contrib import admin
from .models import product, tag, product_category, product_option, product_package, image, rating, configured_product

# Register your models here.
admin.site.register(product)
admin.site.register(tag)
admin.site.register(product_category)
admin.site.register(product_option)
admin.site.register(product_package)
admin.site.register(image)
admin.site.register(rating)
admin.site.register(configured_product)
