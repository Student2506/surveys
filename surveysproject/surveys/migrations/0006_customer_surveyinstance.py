# Generated by Django 2.2.10 on 2021-07-15 04:15

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0005_survey_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('first_name', models.CharField(max_length=20, null=True, verbose_name='Имя пользователя')),
                ('last_name', models.CharField(max_length=20, null=True, verbose_name='Фамилия пользователя')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('results', django.contrib.postgres.fields.jsonb.JSONField()),
                ('survey_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.Survey')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.Customer')),
            ],
        ),
    ]
