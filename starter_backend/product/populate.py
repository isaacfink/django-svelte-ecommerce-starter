from .models import product, product_package, product_category, product_option, configured_product

PRODUCT_DATA = [
    {
        'name': 'outdoor sofa',
        'dscription': 'great sofa to read on',
        'price': 120.00,
        'published': True,
        'in_stock': 10,
        'slug': 'outdoor-sofa',
    },
    {
        'name': 'outdoor chair',
        'dscription': 'great chair to read on',
        'price': 65.00,
        'published': True,
        'in_stock': 17,
        'slug': 'outdoor-chair',
    },
    {
        'name': 'barbeque',
        'dscription': 'perfect meat every time',
        'price': 350.00,
        'published': True,
        'in_stock': 100,
        'slug': 'barbeque',
    },
    {
        'name': 'bicycle rack',
        'dscription': 'won\'t hold your bike but it looks amazing',
        'price': 120.00,
        'published': True,
        'in_stock': 5,
        'slug': 'bicycle-rack',
    },
    {
        'name': 'new item',
        'dscription': 'unpublished item',
        'price': 76.99,
        'published': False,
        'in_stock': 10,
        'slug': 'new-item',
    }
]
def generateProducts():
    for prdct in PRODUCT_DATA:
        p = product.objects.create(
            name=prdct['name'],
            description=prdct['dscription'],
            price=prdct['price'],
            published=prdct['published'],
            in_stock=prdct['in_stock'],
            slug=prdct['slug'],
            category = product_category.objects.get(name='Outdoors'),
        )
        p.save()
