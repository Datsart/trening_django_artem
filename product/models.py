from django.db import models


class Units(models.Model):
    name = models.CharField(max_length=200, verbose_name='Единица измерения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерений'


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название товара')
    amount = models.SmallIntegerField(verbose_name='Количество товаров')
    unit = models.ForeignKey(Units, verbose_name='Единицы измерения', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
