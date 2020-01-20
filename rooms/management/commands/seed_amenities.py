from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):
    help = "This commands creates amenities"

    """  def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="How many times do you want me to tell you that I love you?",
        )
        """

    def handle(self, *args, **options):
        amenities = [
            "Air conditioning",
            "Alarm Clock",
            "Balcony",
            "Bathroom",
            "Bed Linen",
            "kitchen",
            "mount - say",
            "heating",
            "Wireless Internet",
            "Breakfast",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))
