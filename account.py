class Account:

    def __init__(self):
        self._balance = 100
        self.max_balance = 10000

    @property
    def balance(self):
        return self._balance

    def roulette_bet(self):
        self._balance -= 5

    def deposit(self, amount):
        self._balance += amount

    def win(self, amount):
        self._balance += amount

    def place_bet(self, bet_amount):
        self.invalid_bet_message = ''
        if bet_amount <= self._balance:
            self._balance -= bet_amount
        else:
            self.invalid_bet_message = 'You cannot bet more than you have!'

    def __str__(self):
        return '$' + str(self.balance)
