# Generated by Django 5.0.3 on 2024-04-12 10:12

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0036_alter_user_model_id_alter_user_model_referal_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_model',
            name='id',
            field=models.UUIDField(default=uuid.UUID('70ac347d-e305-4cea-a942-bc1fca8331c1'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user_model',
            name='referal_id',
            field=models.UUIDField(default=uuid.UUID('fd452a23-5f98-4063-9dc1-62ad95965a24'), editable=False, unique=True),
        ),
    ]
