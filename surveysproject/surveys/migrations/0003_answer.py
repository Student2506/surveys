# Generated by Django 2.2.10 on 2021-07-14 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0002_auto_20210714_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Введите текст ответа', max_length=60, verbose_name='Ответ')),
                ('question', models.ManyToManyField(related_name='question', to='surveys.Question')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
                'ordering': ('text',),
            },
        ),
    ]
