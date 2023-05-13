from django.db import models


class Rubric(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название Рубрики')

    class Meta:
        verbose_name = 'Название Рубрики'
        verbose_name_plural = 'Названия Рубрик'

    def __str__(self):
        return self.name


# Create your models here.
class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название объявления')
    content = models.TextField(null=True, blank=True, verbose_name='Текст объявления')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    rubric = models.ForeignKey('Rubric', null=True, blank=True, verbose_name='Название Рубрики', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-published']

    def __str__(self):
        return self.title
