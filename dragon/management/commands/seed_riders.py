from model_bakery import baker

from django.core.management.base import BaseCommand

from dragon.models import Dragon, Location, Rider


class Command(BaseCommand):
    help = 'Seed rider initial data'

    def handle(self, *args, **options):
        # Reset data...
        Rider.objects.all().delete()

        riders = baker.make_recipe(
            'dragon.rider',
            _quantity=6
        )

        self.stdout.write("Rider instances created")
