from django.core.management.base import BaseCommand
import openpyxl
from product.models import Product, Units
from tqdm import tqdm


class Command(BaseCommand):
    help = 'Импорт товаров из таблицы'

    def handle(self, *args, **options):
        wb = openpyxl.load_workbook('test1.xlsx')
        ws = wb.active
        total_rows = ws.max_row  # Вычитаем заголовок таблицы
        total_products = 0

        with tqdm(total=total_rows, unit='row') as pbar:
            for row in ws.iter_rows(min_row=0):  # Начинаем с 2 строки, пропуская заголовок таблицы
                name = row[0].value
                amount = row[1].value
                unit = row[2].value
                if not name and not amount and not unit:
                    break
                else:
                    units, _ = Units.objects.get_or_create(name=unit)

                    product = Product.objects.create(
                        title=name,
                        amount=amount,
                        unit=units
                    )
                    total_products += 1
                    pbar.update(1)  # Обновляем прогресс-бар

        self.stdout.write(self.style.SUCCESS(f'Успешно импортировано {total_products} товаров.'))
