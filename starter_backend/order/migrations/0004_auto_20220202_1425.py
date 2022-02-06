# Generated by Django 3.1.14 on 2022-02-02 14:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20220202_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('2145258a-f07f-4477-87a6-ffefa5ad8346'), help_text='uuid field gives each order a unique identifier', unique=True, verbose_name='uuid field'),
        ),
    ]
