from django.test import TestCase

# Create your tests here.
from .models import Car

class CustomUserTests(TestCase):
    def test_create_car(self):
        car = Car.objects.create(brand='Ford',
                                       model='Focus',
                                       generation = 2023,
                                       transmission = "auto",
                                       engine = "benz",
                                       air = 'atmo',
                                       gaz = True,
                                       wheel_drive = 'pered',
                                       capacity = 77,
                                       mileage = 200000,
                                       vincode = 'vincode',
                                       owner = None,
                                       )
        self.assertEqual(car.air, 'atmo')
        self.assertTrue(car.gaz)
