from django.test import TestCase

from trucks.models import Truck, Entry
from datetime import date


class TruckModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all the test methods
        Truck.objects.create(cw=1, truck_number=1, arrival_date=date.today())

    def test_truck_string_representation(self):
        """Test string representation of an truck objects"""
        truck = Truck.objects.get(id=1)
        expected_truck_string_representation = (
            f'CW{truck.cw} - Truck{truck.truck_number}')
        self.assertEqual(str(truck), expected_truck_string_representation)


class TruckEntryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all the test methods
        Truck.objects.create(cw=1, truck_number=1, arrival_date=date.today())
        truck = Truck.objects.get(id=1)
        Entry.objects.create(
            truck=truck, material='194731', material_description='HL-C16/1',
            quantity=1000, weight=100, handling_unit=123456789)

    def test_entry_string_representation(self):
        """Test string representation of entry objects"""
        entry = Entry.objects.get(id=1)
        expected_entry_string_representation = (
            f'{entry.material} - {entry.material_description} - '
            f'{entry.quantity} - {entry.handling_unit}')
        self.assertEqual(str(entry), expected_entry_string_representation)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Entry._meta.verbose_name_plural), "entries")
