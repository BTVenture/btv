# Generated by Django 5.0.3 on 2024-04-17 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0010_rename_product_id_buyed_products_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet_model',
            name='balance_amount',
            field=models.IntegerField(default=0.0),
        ),
    ]
