# Generated by Django 3.1.14 on 2022-02-02 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0003_auto_20220202_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='customer_images',
            field=models.ManyToManyField(blank=True, to='rating.image', verbose_name='customer images'),
        ),
    ]
