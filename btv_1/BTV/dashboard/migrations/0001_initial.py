# Generated by Django 5.0.3 on 2024-04-03 05:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.UUIDField(default=uuid.UUID('c93e9d5a-4c3e-4a49-b1e9-bc40bf84f344'), editable=False, unique=True)),
                ('product_name', models.CharField(max_length=50, unique=True)),
                ('product_price', models.IntegerField(default=0)),
                ('generate_per_day', models.IntegerField(default=0)),
                ('product_image', models.ImageField(upload_to='images/')),
                ('validity_time', models.IntegerField(default=1)),
            ],
        ),
    ]
