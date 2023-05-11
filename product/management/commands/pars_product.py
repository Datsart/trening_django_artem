from django.core.management.base import BaseCommand
import openpyxl


class Command(BaseCommand):
    help = 'Импорт товаров из таблицы'

    def handle(self, *args, **options):
        file_path = 'static/test1.xlsx'  # указываем имя файла
        wb = openpyxl.load_workbook(file_path)
        ws = wb.active

        print("Книга:", wb)
        print("Активный лист:", ws)

        for row in ws.iter_rows(min_row=0):
            name = row[0].value
            if name:
                print("Название товара:", name)
