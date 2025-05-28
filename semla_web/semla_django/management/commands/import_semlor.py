import csv
from django.core.management.base import BaseCommand
from semla_django.models import Semla


class Command(BaseCommand):
    help = 'Importerar semlor från CSV-fil'

    def handle(self, *args, **kwargs):
        with open('semlor.csv', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                price = row['Price'].replace(',', '.')
                Semla.objects.create(
                    bakery=row['Bakery'],
                    city=row['City'],
                    picture=row['Picture'],
                    vegan=(row['Vegan'].strip().upper() == 'T'),
                    price=price,
                    kind=row['Kind']
                )
        self.stdout.write(self.style.SUCCESS('Semlor importerade!'))
