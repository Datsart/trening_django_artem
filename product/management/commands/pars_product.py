from django.core.management.base import BaseCommand
import openpyxl
from product.models import Units, Product


class Command(BaseCommand):
    help = 'Импорт товаров из таблицы'

    def handle(self, *args, **kwargs):
        wb = openpyxl.load_workbook('test.xlsx')
        ws = wb.active
        for lines in ws.iter_rows(min_row=0):
            title = lines[0].value
            amount = lines[1].value
            unit = lines[2].value
            if not title and not amount and not unit:
                pass
            else:
                # Взяли все объекты из модели, проверяем есть ли такой объект в базе,
                # если да - то ничего не делаем, если нет - то создаем такой объект
                units, _ = Units.objects.get_or_create(name=unit)

                product = Product.objects.create(
                    title=title,
                    amount=amount,
                    unit=units,
                )
        self.stdout.write(self.style.SUCCES('Импорт успешно произошел'))