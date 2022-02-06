# Generated by Django 3.1.14 on 2022-02-02 15:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_auto_20220202_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('07102117-df28-4479-9668-2e1cb9a601a3'), help_text='uuid field gives each order a unique identifier', unique=True, verbose_name='uuid field'),
        ),
    ]
