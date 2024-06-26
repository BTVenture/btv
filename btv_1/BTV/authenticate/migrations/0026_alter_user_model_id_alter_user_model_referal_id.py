# Generated by Django 5.0.3 on 2024-04-12 10:05

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0025_alter_user_model_id_alter_user_model_referal_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_model',
            name='id',
            field=models.UUIDField(default=uuid.UUID('7c1be9db-dd72-48b8-b4d6-9d08e245e1a1'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user_model',
            name='referal_id',
            field=models.UUIDField(default=uuid.UUID('f6990959-479f-40ae-bbab-6e253f60cfc6'), editable=False, unique=True),
        ),
    ]
