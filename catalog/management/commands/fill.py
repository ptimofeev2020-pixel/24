from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Удаляет данные и заполняет базу тестовыми категориями и продуктами из фикстур'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command('loaddata', 'category.json')
        call_command('loaddata', 'product.json')

        self.stdout.write(self.style.SUCCESS('Данные успешно загружены'))
