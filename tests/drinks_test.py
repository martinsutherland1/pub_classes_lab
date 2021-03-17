import unittest

from src.drinks import Drinks


class TestDrinks(unittest.TestCase):

    def setUp(self):
        self.drinks = Drinks("Beer", 5.00, 2.8)

    def test_drink_has_name(self):
        self.assertEqual("Beer", self.drinks.name)

    def test_drink_has_price(self):
        self.assertEqual(5.00, self.drinks.price)

    def test_drink_has_alcohol_level(self):
        self.assertEqual(2.8, self.drinks.alcohol_level)
