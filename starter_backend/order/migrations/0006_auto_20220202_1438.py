# Generated by Django 3.1.14 on 2022-02-02 14:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20220202_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('b6c1bd72-6819-44a8-bc58-ec4194c268eb'), help_text='uuid field gives each order a unique identifier', unique=True, verbose_name='uuid field'),
        ),
    ]
