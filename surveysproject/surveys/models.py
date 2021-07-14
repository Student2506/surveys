from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Survey(models.Model):
    name = models.TextField('Название опроса',
                            max_length=40,
                            help_text='Дайте имя опросу')
    start_date = models.DateTimeField('Старт опроса', auto_now_add=True)
    end_date = models.DateTimeField('Окончание опроса',
                                    null=True,
                                    blank=True,
                                    help_text='Укажите дату окончания')
    description = models.TextField('Описание',
                                   null=True,
                                   blank=True,
                                   help_text='Задайте описание')

    class Meta:
        ordering = ('-start_date', )
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.name[:15]


class Question(models.Model):
    TEXT = 'txt'
    SINGLE = 'sng'
    MULTIPLE = 'mul'
    QUESTION_TYPE = [
        (TEXT, 'Ответ текстом'),
        (SINGLE, 'Выбор одного варианта'),
        (MULTIPLE, 'Несколько вариантов'),
    ]
    text = models.TextField('Вопрос опросника',
                            max_length=60,
                            help_text='Введите суть вопроса')
    survey = models.ForeignKey(Survey,
                               on_delete=models.CASCADE,
                               related_name='questions')
    type = models.CharField('Тип вопроса',
                            max_length=3,
                            choices=QUESTION_TYPE,
                            default=TEXT)

    class Meta:
        ordering = ('-survey', )
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text[:15]


class Answer(models.Model):
    text = models.TextField('Ответ',
                            max_length=60,
                            help_text='Введите текст ответа')
    question = models.ManyToManyField(Question, related_name='answers')

    class Meta:
        ordering = ('text', )
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.text[:15]
