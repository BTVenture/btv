# Generated by Django 5.0.3 on 2024-04-03 05:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0012_user_model_refered_by_alter_user_model_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_model',
            name='id',
            field=models.UUIDField(default=uuid.UUID('c1908b03-1e47-4508-a5d3-81f48bddebaf'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user_model',
            name='referal_id',
            field=models.UUIDField(default=uuid.UUID('24c3c463-7646-4ceb-b71b-c40f135476f7'), editable=False, unique=True),
        ),
    ]