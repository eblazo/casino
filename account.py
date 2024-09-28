class Account:

    def __init__(self):
        self._balance = 100
        self.max_balance = 10000

    @property
    def balance(self):
        return self._balance

    def add_twenty(self):
        self._balance += 20

    def add_fifty(self):
        self._balance += 50

    def add_hundred(self):
        self._balance += 100

    def __str__(self):
        return '$' + str(self.balance)


