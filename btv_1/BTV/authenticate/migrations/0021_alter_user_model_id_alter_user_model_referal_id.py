# Generated by Django 5.0.3 on 2024-04-11 09:37

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0020_alter_user_model_id_alter_user_model_referal_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_model',
            name='id',
            field=models.UUIDField(default=uuid.UUID('965856a2-2433-4ae8-856e-b9b1274ba317'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user_model',
            name='referal_id',
            field=models.UUIDField(default=uuid.UUID('7814b0cc-522d-4c0d-961c-a0cdfba5f1c3'), editable=False, unique=True),
        ),
    ]
