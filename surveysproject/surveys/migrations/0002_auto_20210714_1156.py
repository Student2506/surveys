# Generated by Django 2.2.10 on 2021-07-14 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('-survey',), 'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.AlterModelOptions(
            name='survey',
            options={'ordering': ('-start_date',), 'verbose_name': 'Опрос', 'verbose_name_plural': 'Опросы'},
        ),
    ]
