import unittest
from haversine_coverage import haversine_coverage
from haversine import haversine

class HaversineCoverageTest(unittest.TestCase):

    def test_coverage_shopper(self):
        location = [(45.35, 10.84)] 
        shoppers = [
            {'id': 'S1', 'lat': 45.46, 'lng': 11.03, 'enabled': True}
        ]

        result = haversine_coverage(location, shoppers)

        expected = [
            {'shopper_id': 'S1', 'coverage': 0}
        ]
        self.assertEqual(result , expected)

    def test_coverage_shopper_not_enabled(self):
        location = [(45.35, 10.84)] 
        shoppers = [
            {'id': 'S1', 'lat': 45.46, 'lng': 11.03, 'enabled': False}
        ]

        result = haversine_coverage(location, shoppers)

        self.assertEqual(result , [])


if __name__ == "__main__":
    unittest.main()

