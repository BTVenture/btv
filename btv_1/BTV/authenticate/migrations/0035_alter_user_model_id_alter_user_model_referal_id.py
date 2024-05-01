# Generated by Django 5.0.3 on 2024-04-12 10:11

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0034_alter_user_model_id_alter_user_model_referal_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_model',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user_model',
            name='referal_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]