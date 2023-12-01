from django.db import models
from django.core import validators


class Rubric(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название Рубрики')

    class Meta:
        verbose_name = 'Название Рубрики'
        verbose_name_plural = 'Названия Рубрик'

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # добавил интернет-адрес модели --> в шаблоне смотри
        return '/qwert/%s/' % self.pk


# Create your models here.
class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название объявления',
                             validators=[validators.RegexValidator(regex='^.{4,}$')],
                             error_messages={'invalid': 'Длина не менее 4х символов'})
    # валидатор на проверку - начинается и зканчивается строкой, минимум 4 символа

    content = models.TextField(null=True, blank=True, verbose_name='Текст объявления', validators=[
        validators.MinLengthValidator(3, message='Длина не менее 3х символов')])
    # валидатор на минимум 3 символа

    price = models.PositiveIntegerField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    rubric = models.ForeignKey('Rubric', null=False, blank=False, verbose_name='Название Рубрики',
                               on_delete=models.PROTECT)

    # создание списка действий

    KINDS = (
        (None, 'Выберете действие'),
        ('s', 'куплю'),
        ('v', 'продам'),
        ('c', 'обменяю'),
    )

    kind = models.CharField(max_length=1, choices=KINDS, default='s', verbose_name='Действие')

    def get_kind_display(self):
        return dict(self.KINDS).get(self.kind, '')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-published']

    def __str__(self):
        return self.title

    def title_and_price(self):  # метод для вывода цены и названия в одном теге
        if self.price:
            return '%s - %i р.' % (self.title, self.price)
        else:
            return self.title

    title_and_price.short_description = 'Название и цена'  # это надо добавить в админку для отображения
