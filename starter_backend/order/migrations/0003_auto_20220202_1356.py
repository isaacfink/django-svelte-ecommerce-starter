# Generated by Django 3.0 on 2022-02-02 13:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20220202_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('e815ea21-cccf-4597-a404-fa90cd3923a0'), help_text='uuid field gives each order a unique identifier', unique=True, verbose_name='uuid field'),
        ),
    ]
