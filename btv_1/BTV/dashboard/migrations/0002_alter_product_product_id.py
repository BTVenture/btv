# Generated by Django 5.0.3 on 2024-04-03 06:00

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.UUIDField(default=uuid.UUID('8e81a3b5-0c9b-4674-9b9c-4604a8f63a27'), editable=False, unique=True),
        ),
    ]
