# Generated by Django 3.1.14 on 2022-02-02 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
        ('users', '0004_auto_20220202_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='payments',
            field=models.ManyToManyField(blank=True, related_name='payments', to='payment.method', verbose_name='payment methods'),
        ),
    ]
