# Generated by Django 5.0.3 on 2024-04-12 10:10

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0033_alter_user_model_id_alter_user_model_referal_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_model',
            name='id',
            field=models.UUIDField(default=uuid.UUID('01949221-2625-43c7-85ed-6a78c14fd7d5'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user_model',
            name='referal_id',
            field=models.UUIDField(default=uuid.UUID('0637c3af-d13e-4cfe-9436-bf25d57edf6d'), editable=False, unique=True),
        ),
    ]
