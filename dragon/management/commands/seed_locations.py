from model_bakery import baker

from django.core.management.base import BaseCommand

from dragon.models import Dragon, Location, Rider


class Command(BaseCommand):
    help = 'Seed location initial data'

    def handle(self, *args, **options):
        # Reset data...
        Location.objects.all().delete()

        # Create instances
        Location.objects.create(name="Dragonstone")
        Location.objects.create(name="King's Landing")

        self.stdout.write("Location instances created")
