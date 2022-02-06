# Generated by Django 3.0 on 2022-02-02 13:55

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payment', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_1', models.CharField(help_text='street address one', max_length=250, verbose_name='street address 1')),
                ('street_2', models.CharField(blank=True, help_text='street address two', max_length=250, null=True, verbose_name='street address 2')),
                ('postal_code', models.IntegerField(help_text='address zipcode', verbose_name='address zipcode')),
                ('city', models.CharField(help_text='address city', max_length=100, verbose_name='address city')),
                ('state', models.CharField(help_text='address state', max_length=50, verbose_name='address state')),
                ('country', models.CharField(help_text='address country', max_length=100, verbose_name='address country')),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'adresses',
            },
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='customer first name', max_length=100, verbose_name='customer first name')),
                ('last_name', models.CharField(help_text='customer last name', max_length=100, verbose_name='customer last name')),
                ('phone_number', models.BigIntegerField(help_text='customer phone number', verbose_name='customer phone number')),
                ('addresses', models.ManyToManyField(related_name='customer_addresses', to='users.address', verbose_name='customer addresses')),
                ('default_billing_address', models.ForeignKey(blank=True, help_text='default address for new payment methods', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='default_billing', to='users.address', verbose_name='default billing address')),
                ('default_payment', models.ForeignKey(blank=True, help_text='default payment for new orders', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='default_payment', to='payment.method', verbose_name='default payment')),
                ('default_shipping_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='default_shipping', to='users.address', verbose_name='default shipping address')),
                ('payments', models.ManyToManyField(related_name='payments', to='payment.method', verbose_name='payment methods')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='customer user account')),
            ],
        ),
    ]
