# Generated by Django 2.2.10 on 2021-07-14 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0003_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ManyToManyField(related_name='answers', to='surveys.Question'),
        ),
    ]
