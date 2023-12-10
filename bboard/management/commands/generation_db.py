from faker import Faker
from bboard.models import Bb, Rubric
from django.core.management.base import BaseCommand

fake = Faker()


class Command(BaseCommand):
    help = 'Генерация данных'

    def handle(self, *args, **options):
        for i in range(10):
            rubric = Rubric.objects.create(name=fake.word())  # Создайте экземпляр Rubric
            ad = Bb(
                title=fake.sentence(),
                content=fake.paragraph(),
                price=fake.random_int(min=100, max=1000, step=50),
                rubric=rubric,  # Присвойте экземпляр Rubric в поле rubric
            )
            ad.save()
        self.stdout.write(self.style.SUCCESS('Данные сгенерированы'))
