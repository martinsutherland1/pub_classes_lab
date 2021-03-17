import unittest

from src.customer import Customer
from src.drinks import Drinks
from src.food import Food


class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Colin", 8.50, 27)
        self.drink = Drinks("wine", 6.50, 4)
        self.food = Food('kebab', 6.00, 4)

    def test_customer_has_name(self):
        self.assertEqual("Colin", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(8.50, self.customer.wallet)

    def test_customer_has_age(self):
        self.assertEqual(27, self.customer.age)

    def test_reduce_wallet_drink(self):
        self.customer.reduce_wallet(self.drink.price)
        self.assertEqual(2, self.customer.wallet)

    def test_drunkenness_increase(self):
        self.customer.increase_drunkenness(self.drink.alcohol_level)
        self.assertEqual(4, self.customer.drunkenness)

    def test_reduce_wallet_food(self):
        self.customer.reduce_wallet(self.food.price)
        self.assertEqual(2.50, self.customer.wallet)
