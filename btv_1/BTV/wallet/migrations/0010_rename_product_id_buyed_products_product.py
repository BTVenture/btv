# Generated by Django 5.0.3 on 2024-04-16 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0009_buyed_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyed_products',
            old_name='product_id',
            new_name='product',
        ),
    ]