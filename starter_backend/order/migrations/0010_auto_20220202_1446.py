# Generated by Django 3.1.14 on 2022-02-02 14:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_auto_20220202_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('25c4aa97-e727-4ab3-925d-e88d22346f4c'), help_text='uuid field gives each order a unique identifier', unique=True, verbose_name='uuid field'),
        ),
    ]
