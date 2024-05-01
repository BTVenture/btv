# Generated by Django 5.0.3 on 2024-04-11 09:24

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0019_alter_user_model_id_alter_user_model_referal_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_model',
            name='id',
            field=models.UUIDField(default=uuid.UUID('cc12feda-65df-41fa-901e-5b1566ee8f52'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user_model',
            name='referal_id',
            field=models.UUIDField(default=uuid.UUID('c2797bc5-18f5-4086-8d8c-3122bf907638'), editable=False, unique=True),
        ),
    ]
