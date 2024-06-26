# Generated by Django 5.0.3 on 2024-03-31 08:19

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_model',
            name='email_token',
            field=models.UUIDField(default=uuid.UUID('3b2f85f5-618c-44bb-8bc2-9f1c7edb6dc3'), editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user_model',
            name='id',
            field=models.UUIDField(default=uuid.UUID('9c4653d1-68c3-4bfd-829f-e7a51744e4f5'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
