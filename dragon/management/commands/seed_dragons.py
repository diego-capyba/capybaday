import random
from model_bakery import baker

from django.core.management.base import BaseCommand

from dragon.models import Dragon, Location, Rider


class Command(BaseCommand):
    help = 'Seed dragons initial data'

    def add_arguments(self, parser):
        parser.add_argument('n_dragons', type=int)

    def handle(self, *args, **options):
        # Reset data...
        Dragon.objects.all().delete()

        # Create instances
        locations = Location.objects.all()
        riders = Rider.objects.all()
        dragons = baker.make_recipe(
            'dragon.dragon',
            location=lambda: random.choice(locations),
            _quantity=options['n_dragons']
        )
        for d in dragons:
            d.riders.set(random.sample(set(riders), 3))

        self.stdout.write("Dragon instances created")
