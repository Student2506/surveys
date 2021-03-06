# Generated by Django 2.2.10 on 2021-07-14 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='Дайте имя опросу', max_length=40, verbose_name='Название опроса')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='Старт опроса')),
                ('end_date', models.DateTimeField(blank=True, help_text='Укажите дату окончания', null=True, verbose_name='Окончание опроса')),
                ('description', models.TextField(blank=True, help_text='Задайте описание', null=True, verbose_name='Описание')),
            ],
            options={
                'ordering': ('-start_date',),
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Введите суть вопроса', max_length=60, verbose_name='Вопрос опросника')),
                ('type', models.CharField(choices=[('txt', 'Ответ текстом'), ('sng', 'Выбор одного варианта'), ('mul', 'Несколько вариантов')], default='txt', max_length=3, verbose_name='Тип вопроса')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='surveys.Survey')),
            ],
            options={
                'ordering': ('-survey',),
            },
        ),
    ]
