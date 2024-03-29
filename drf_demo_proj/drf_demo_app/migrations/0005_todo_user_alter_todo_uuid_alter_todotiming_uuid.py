# Generated by Django 5.0.1 on 2024-01-05 11:17

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_demo_app', '0004_alter_todo_uuid_todotiming'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('67e2d1b9-d110-4293-8767-affe7839e6fe'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todotiming',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('67e2d1b9-d110-4293-8767-affe7839e6fe'), editable=False, primary_key=True, serialize=False),
        ),
    ]
