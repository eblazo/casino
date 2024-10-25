class Account:
    """
    Represents a player's account for managing their balance in a casino game.

    Attributes:
        _balance (int): The current balance of the account, initialized to 100.
        _invalid_bet_message (str): Message indicating if a bet is invalid.

    Methods:
        balance: Property that returns the current balance of the account.
        roulette_bet: Deducts a fixed amount (5) from the account balance for a roulette bet.
        deposit(amount): Increases the account balance by the specified amount.
        place_bet(bet_amount): Deducts the specified bet amount from the balance if sufficient funds
                               are available. If the bet amount exceeds the balance,
                               an error message is set.
        __str__(): Returns a string representation of the account balance in dollar format.
    """

    def __init__(self):
        """
        Initializes a new Account instance with a balance of 100 and an empty invalid bet message.
        """
        self._balance = 100
        self._invalid_bet_message = ''

    @property
    def balance(self):
        """
        Gets the current balance of the account.

        Returns:
            int: The current balance.
        """
        return self._balance

    @property
    def invalid_bet_message(self):
        """
        Tells the user that a bet is invalid if it is more than their account balance.

        Returns:
            str: A message stating that the bet is invalid.
                """
        return self._invalid_bet_message

    def roulette_bet(self):
        """
        Deducts a fixed amount (5) from the account balance for a roulette bet.
        """
        self._balance -= 5

    def deposit(self, amount):
        """
        Increases the account balance by the specified amount.

        Args:
            amount (int): The amount to be added to the balance.
        """
        self._balance += amount

    def place_bet(self, bet_amount):
        """
        Deducts the specified bet amount from the balance if sufficient funds are available.
        If the bet amount exceeds the balance, an error message is set.

        Args:
            bet_amount (int): The amount to bet.

        Sets:
            invalid_bet_message (str): A message indicating if the bet is invalid.
        """
        if bet_amount <= self._balance:
            self._invalid_bet_message = ''
            self._balance -= bet_amount
        else:
            self._invalid_bet_message = 'You cannot bet more than you have!'

    def __str__(self):
        """
        Returns a string representation of the account balance in dollar format.

        Returns:
            str: A string representing the account balance.
        """
        return '$' + str(self.balance)
