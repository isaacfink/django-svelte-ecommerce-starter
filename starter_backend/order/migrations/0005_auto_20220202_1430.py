# Generated by Django 3.1.14 on 2022-02-02 14:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20220202_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('1cc0a2d9-a8ea-4d6a-82dd-6bb912c3e493'), help_text='uuid field gives each order a unique identifier', unique=True, verbose_name='uuid field'),
        ),
    ]