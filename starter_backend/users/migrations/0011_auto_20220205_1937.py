# Generated by Django 3.1.14 on 2022-02-05 19:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20220205_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, help_text='uuid field gives each customer a unique identifier', unique=True, verbose_name='uuid field'),
        ),
    ]