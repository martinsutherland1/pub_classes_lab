class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def increase_drunkenness(self, units):
        self.drunkenness += units

    def decrease_drunkenness(self, unit):
        self.drunkenness -= unit
