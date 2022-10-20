from model_bakery import baker

from django.core.management.base import BaseCommand

from dragon.models import Dragon, Location, Rider


class Command(BaseCommand):
    help = 'Seed rider initial data'

    def handle(self, *args, **options):
        # Reset data...
        Rider.objects.all().delete()

        # Create instances
        Rider.objects.create(name="Aegon")
        Rider.objects.create(name="Viserys I")
        Rider.objects.create(name="Rhaenyra")
        Rider.objects.create(name="Daemon")
        Rider.objects.create(name="Jon Snow")
        Rider.objects.create(name="Daenerys")

        print("Rider instances created")
