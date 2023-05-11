from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Импорт товаров из таблицы'
    def handle(self, *args, **kwargs):
        pass
