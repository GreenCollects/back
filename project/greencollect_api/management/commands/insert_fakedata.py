from django.core.management.base import BaseCommand
from greencollect_api.models import Waste, Point
from django.db.utils import IntegrityError
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Insert entity in data base'

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--superuser',
            action='store_true',
            help='Insert only the superuser',
        )

    def handle(self, *args, **kwargs):
        self.stdout.write("Insert fake data in database")
        if kwargs['superuser']:
            self.insertSuperUser()
        else:
            self.insertSuperUser()
            self.insertWaste()
            self.insertPoint()

    def insertSuperUser(self):
        self.stdout.write("Insert super user...")
        try:
            user=User.objects.create_user(username='admin', password='admin', email='superuser@greencollect.fr')
            user.is_superuser=True
            user.is_staff=True
            user.save()
        except IntegrityError:
            self.stdout.write("Super user already exist in database")
        
        self.stdout.write("End of insertion")

    def insertWaste(self):
        self.stdout.write("Insert Waste...")
        try:
            Waste.objects.create(label='Piles')
            Waste.objects.create(label='Batteries')
            Waste.objects.create(label='Huiles')
            Waste.objects.create(label='Pneus')
            Waste.objects.create(label='Électroménagers')
        except IntegrityError:
            self.stdout.write("Waste data already exist in database")

        self.stdout.write("End of insertion")

    def insertPoint(self):
        self.stdout.write("Insert Point...")
        LATITUDE = 45.188529
        LONGITUDE = 5.724524
        try:
            point = Point.objects.create(label='Point1', latitude=LATITUDE, longitude=LONGITUDE)
            point.wastes.set([1,2])
            point = Point.objects.create(label='Point2', latitude=LATITUDE-0.004, longitude=LONGITUDE-0.004)
            point.wastes.set([2,3])
            point = Point.objects.create(label='Point3', latitude=LATITUDE+0.004, longitude=LONGITUDE-0.004)
            point.wastes.set([1,3])
        except IntegrityError:
            self.stdout.write("Point data already exist in database")

        self.stdout.write("End of insertion")