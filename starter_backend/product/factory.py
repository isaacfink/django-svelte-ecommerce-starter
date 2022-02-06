import factory
from .models import product, product_category, product_option, configured_product

from .models import User

# product factory
class productFactory(factory.Factory):
    class Meta:
        model = product

    name = factory.Faker('name')
    description = factory.Faker('text')
    price = factory.Faker('random_number', digits=4)
    published = factory.Faker('boolean')
    in_stock = factory.Faker('random_number', digits=4)