# Generated by Django 5.0.3 on 2024-03-31 08:21

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0002_user_model_email_token_alter_user_model_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_model',
            name='email_token',
            field=models.UUIDField(default=uuid.UUID('7f0af4c9-5ef7-46cc-92c4-ae9a15d009b0'), editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user_model',
            name='id',
            field=models.UUIDField(default=uuid.UUID('7d2177d4-3e0b-4f1e-8b5e-fbd7f908c2ba'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
