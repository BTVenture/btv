# Generated by Django 5.0.3 on 2024-04-03 06:14

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0015_alter_user_model_id_alter_user_model_referal_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_model',
            name='id',
            field=models.UUIDField(default=uuid.UUID('02460d7b-7170-4d6e-8f42-c811e170481e'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user_model',
            name='referal_id',
            field=models.UUIDField(default=uuid.UUID('898f4a47-b51e-4a49-b052-b562fe31cf4c'), editable=False, unique=True),
        ),
    ]
