# Generated by Django 5.0.1 on 2024-01-04 22:17

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_demo_app', '0003_remove_todo_uid_todo_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('8cf80e51-dd74-424c-b359-247448acf2ca'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='TodoTiming',
            fields=[
                ('uuid', models.UUIDField(default=uuid.UUID('8cf80e51-dd74-424c-b359-247448acf2ca'), editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('timing', models.DateField()),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drf_demo_app.todo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]