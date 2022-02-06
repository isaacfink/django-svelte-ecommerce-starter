from .models import User, customer, address
import requests

API_URL = 'https://randomuser.me/api/'



def generateUsers(amount=100):
    API_DATA = {'results':amount, 'nat': 'US'}
    user_request = requests.get(API_URL, params=API_DATA)

    user_data = user_request.json()

    for user in user_data['results']:
        user_instance = User.objects.create(
            username= user['login']['username'],
            email = user['email'],
        )
        user_instance.set_password(
            raw_password = user['login']['password']
        )
        user_instance.save()

        customer_address = address.objects.create(
            street_1 = str(user['location']['street']['number']) + ' ' + user['location']['street']['name'],
            city = user['location']['city'],
            state = user['location']['state'],
            postal_code = user['location']['postcode'],
            country = 'USA',
        )

        customer_instance = customer.objects.create(
            user = user_instance,
            first_name = user['name']['first'],
            last_name = user['name']['last'],
            phone_number = int(user['phone'].replace('-','').replace('(','').replace(')','').replace(' ','')),
            email_address = user['email'],

        )

        customer_instance.addresses.add(customer_address)

        customer_address.save()
        customer_instance.save()

