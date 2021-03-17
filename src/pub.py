class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.stock = {}

    def increase_till_cash(self, amount):
        self.till += amount

    def check_age(self, customer_age):
        return customer_age >= 18

    def check_drunkeness(self, customer_drunkenness):
        return customer_drunkenness < 40

    def add_to_stock(self, drink):
        if drink in self.stock:
            self.stock[drink] += 1
        else:
            self.stock[drink] = 1

    def stock_value(self):
        total = 0

        for drink in self.stock:
            total += (drink.price * self.stock[drink])

        return total
