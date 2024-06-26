# Generated by Django 5.0.3 on 2024-04-12 10:14

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0038_alter_user_model_id_alter_user_model_referal_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_model',
            name='id',
            field=models.UUIDField(default=uuid.UUID('48649f30-afa4-4006-b6f9-c3c01f5b14a0'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user_model',
            name='referal_id',
            field=models.UUIDField(default=uuid.UUID('7c1acad8-39ff-485f-bb57-97a939fff710'), editable=False, unique=True),
        ),
    ]
