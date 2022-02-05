from django.test import TestCase
from django.urls import reverse

from trucks.models import Truck
from datetime import date


class TruckListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 trucks for pagination tests
        number_of_trucks = 13

        for truck_id in range(number_of_trucks):
            Truck.objects.create(
                cw=truck_id, truck_number=1, arrival_date=date.today())

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/trucks/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('trucks:trucks'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('trucks:trucks'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trucks/index.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('trucks:trucks'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['truck_list']), 10)

    def test_lists_all_authors(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('trucks:trucks')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['truck_list']), 3)


class AddTruckViewTest(TestCase):
    pass
