from django.db import models


class Rubric(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название Рубрики')

    class Meta:
        verbose_name = 'Название Рубрики'
        verbose_name_plural = 'Названия Рубрик'

    def __str__(self):
        return self.name

    def get_absolute_url(self): # добавил интернет-адрес модели --> в шаблоне смтори
        return '/qwert/%s/' % self.pk


# Create your models here.
class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название объявления')
    content = models.TextField(null=True, blank=True, verbose_name='Текст объявления')
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
