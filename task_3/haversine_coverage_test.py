import unittest
from haversine_coverage import haversine_coverage

locations = [
    	  {'id': 1000, 'zip_code': '37069', 'lat': 45.35, 'lng': 10.84},
    	  {'id': 1001, 'zip_code': '37121', 'lat': 45.44, 'lng': 10.99},
    	  {'id': 1001, 'zip_code': '37129', 'lat': 45.44, 'lng': 11.00},
          {'id': 1001, 'zip_code': '37133', 'lat': 45.43, 'lng': 11.02},
]

shoppers = [
    {'id': 'S1', 'lat': 45.46, 'lng': 11.03, 'enabled': True},
    {'id': 'S2', 'lat': 45.46, 'lng': 10.12, 'enabled': True},
    {'id': 'S3', 'lat': 45.34, 'lng': 10.81, 'enabled': True},
    {'id': 'S4', 'lat': 45.76, 'lng': 10.57, 'enabled': True},
    {'id': 'S5', 'lat': 45.34, 'lng': 10.63, 'enabled': True},
    {'id': 'S6', 'lat': 45.42, 'lng': 10.81, 'enabled': True},
    {'id': 'S7', 'lat': 45.34, 'lng': 10.94, 'enabled': True},
]

class HaversineCoverageTest(unittest.TestCase):

    def test_haversine_coverage_shopper(self):
        location = [locations[0]]
        shopper = [
            {'id': 'S1', 'lat': 45.46, 'lng': 11.03, 'enabled': True}
        ]

        shoppers_coverage = haversine_coverage(location, shopper)

        expected = [
            {'shopper_id': 'S1', 'coverage': 0}
        ]
        self.assertEqual(shoppers_coverage, expected)

    def test_haversine_coverage_shopper_not_enabled(self):
        location = [locations[0]] 
        shoppers = [
            {'id': 'S1', 'lat': 45.46, 'lng': 11.03, 'enabled': False}
        ]

        shoppers_coverage = haversine_coverage(location, shoppers)

        self.assertEqual(shoppers_coverage, [])

    def test_haversine_coverage_shoppers_with_multiple_locations(self):
        location = [locations[0], locations[1]]
        shoppers = [
            {'id': 'S1', 'lat': 45.46, 'lng': 11.03, 'enabled': True},
            {'id': 'S2', 'lat': 45.46, 'lng': 10.12, 'enabled': True},
        ]

        shoppers_coverage = haversine_coverage(location, shoppers)

        expected = [
            {'shopper_id': 'S1', 'coverage': 50},
            {'shopper_id': 'S2', 'coverage': 0},
        ]
        self.assertEqual(shoppers_coverage, expected)

    def test_all_shoppers_with_all_locations(self):
        shoppers_coverage = haversine_coverage(locations, shoppers)

        expected = [
            {'shopper_id': 'S1', 'coverage': 75},
            {'shopper_id': 'S3', 'coverage': 25},
            {'shopper_id': 'S6', 'coverage': 25},
            {'shopper_id': 'S7', 'coverage': 25},
            {'shopper_id': 'S2', 'coverage': 0},
            {'shopper_id': 'S4', 'coverage': 0},
            {'shopper_id': 'S5', 'coverage': 0}
        ]
        self.assertEqual(shoppers_coverage, expected)

if __name__ == "__main__":
    unittest.main()

