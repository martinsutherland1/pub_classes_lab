import unittest

from src.pub import Pub
from src.drinks import Drinks
from src.customer import Customer
from src.food import Food


class TestPub(unittest.TestCase):

    def setUp(self):
        self.drink_1 = Drinks("beer", 4.00, 5)
        self.drink_2 = Drinks("wine", 6.50, 10)
        self.drink_3 = Drinks("gin", 4.00, 30)
        self.pub = Pub("The Prancing Pony", 100.00)
        self.customer = Customer("Colin", 8.50, 27)
        self.food = Food("kebab", 6.00, 4)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_till_increases_drink(self):
        self.pub.increase_till_cash(self.drink_1.price)
        self.assertEqual(104.00, self.pub.till)

    def test_age_check(self):
        check = self.pub.check_age(self.customer.age)
        self.assertEqual(True, check)

    def test_sober(self):
        check = self.pub.check_drunkeness(self.customer.drunkenness)
        self.assertEqual(True, check)

    def test_pub_till_increases_food(self):
        self.pub.increase_till_cash(self.food.price)
        self.assertEqual(106.00, self.pub.till)

    def test_add_stock(self):
        self.pub.add_to_stock(self.drink_1)
        self.assertEqual(1, len(self.pub.stock))

    def test_pub_has_stock_value(self):
        self.pub.add_to_stock(self.drink_1)
        self.assertEqual(4.00, self.pub.stock_value())
