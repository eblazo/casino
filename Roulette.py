import random


class Roulette:
    """
    Represents a game of Roulette, allowing players to place bets on various positions
    on the roulette table and spin the wheel to determine winning bets.

    Attributes:
        _roulette_payout (dict): A mapping of positions to their corresponding payout values.
        _red_numbers (list): A list of numbers that are colored red on the roulette wheel.
        _black_numbers (list): A list of numbers that are colored black on the roulette wheel.
        _top_row (list): A list of numbers that make up the top row of the roulette table.
        _middle_row (list): A list of numbers that make up the middle row of the roulette table.
        _bottom_row (list): A list of numbers that make up the bottom row of the roulette table.
        _num_bets (int): The current number of bets placed by the player.
        _max_bets (int): The maximum number of bets allowed in a single round.
        _has_spun (bool): A flag indicating whether the roulette wheel has been spun.
        _landing_number (int): The number on which the roulette ball lands.
        _roulette_positions (dict): A mapping of positions to the amounts bet on them.

    Methods:
        bet_position(position, account): Places a bet on a specified position and updates the player's account.
        payout(): Calculates the total winnings based on the bets placed and the landing number.
        reset(): Resets the game state, clearing all bets and spin results.
        spin(): Spins the roulette wheel, generating a random landing number.
        bets_text(): Returns a list of current bets and their amounts in a readable format.
        landed_on_color(): Determines the color of the number the ball landed on.
    """

    _roulette_payout = {
        "0": 35, "1": 35, "2": 35, "3": 35, "4": 35, "5": 35,
        "6": 35, "7": 35, "8": 35, "9": 35, "10": 35, "11": 35,
        "12": 35, "13": 35, "14": 35, "15": 35, "16": 35, "17": 35,
        "18": 35, "19": 35, "20": 35, "21": 35, "22": 35, "23": 35,
        "24": 35, "25": 35, "26": 35, "27": 35, "28": 35, "29": 35,
        "30": 35, "31": 35, "32": 35, "33": 35, "34": 35, "35": 35,
        "36": 35,
        "top 2-1": 2,
        "mid 2-1": 2,
        "bot 2-1": 2,
        "first 12": 2,
        "second 12": 2,
        "third 12": 2,
        "1-18": 1,
        "even": 1,
        "red": 1,
        "black": 1,
        "odd": 1,
        "19-36": 1
    }
    _red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    _black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

    _top_row = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
    _middle_row = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
    _bottom_row = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]

    def __init__(self):
        """Initialize the Roulette game with default settings."""
        self._num_bets = 0
        self._max_bets = 3
        self._has_spun = False
        self._landing_number = -1
        self._roulette_positions = {
            "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0,
            "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0,
            "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0,
            "18": 0, "19": 0, "20": 0, "21": 0, "22": 0, "23": 0,
            "24": 0, "25": 0, "26": 0, "27": 0, "28": 0, "29": 0,
            "30": 0, "31": 0, "32": 0, "33": 0, "34": 0, "35": 0,
            "36": 0,
            "top 2-1": 0,
            "mid 2-1": 0,
            "bot 2-1": 0,
            "first 12": 0,
            "second 12": 0,
            "third 12": 0,
            "1-18": 0,
            "even": 0,
            "red": 0,
            "black": 0,
            "odd": 0,
            "19-36": 0
        }

    def bet_position(self, position, account):
        """
        Place a bet on a specific position on the roulette table.

        Parameters:
        position (str): The position to place the bet on.
        account (Account): The player's account for placing the bet.
        """
        if self._num_bets < self._max_bets:
            self._roulette_positions[position] += 5
            account.roulette_bet()
            self._num_bets += 1

    @property
    def num_bets(self):
        """Return the current number of bets placed."""
        return self._num_bets

    @property
    def max_bets(self):
        """Return the maximum number of bets allowed in the game."""
        return self._max_bets

    @property
    def landing_number(self):
        """Return the number where the roulette ball landed."""
        return self._landing_number

    @property
    def red_numbers(self):
        """Return a list of the red numbers on the roulette wheel."""
        return self._red_numbers

    @property
    def has_spun(self):
        """Check if the roulette wheel has been spun."""
        return self._has_spun

    def bets_text(self):
        """
        Return a list of current bets placed and their amounts as text.

        Returns:
        list: A list of bet descriptions as strings.
        """
        bet_text = []
        for key in self._roulette_positions:
            if self._roulette_positions[key] > 0:
                bet_text.append(str(key) + ": $" + str(self._roulette_positions[key]))
        return bet_text

    def payout(self):
        """
        Calculate the total winnings based on the bets placed and where the ball landed.

        Returns:
        int: The total amount of money won from all the bets.
        """
        total_winnings = 0
        for position in self._roulette_positions:
            if self._roulette_positions[position] > 0:
                position_winnings = 0
                # Tests if the ball landed on the exact number
                if self._landing_number == position:
                    position_winnings += (self._roulette_payout[position]) * self._roulette_positions[position]
                if position == "red" and self._landing_number in self._red_numbers:
                    position_winnings += (self._roulette_payout[position]) * self._roulette_positions[position]
                if position == "black" and self._landing_number in self._black_numbers:
                    position_winnings += (self._roulette_payout[position]) * self._roulette_positions[position]
                if position == "even" and self._landing_number % 2 == 0:
                    position_winnings += (self._roulette_payout[position]) * self._roulette_positions[position]
                if position == "odd" and self._landing_number % 2 == 1:
                    position_winnings += (self._roulette_payout[position]) * self._roulette_positions[position]
                if position == "1-18" and self._landing_number in range(1, 19):
                    position_winnings += (self._roulette_payout[position]) * self._roulette_positions[position]
                if position == "19-36" and self._landing_number in range(19, 37):
                    position_winnings += (self._roulette_payout[position]) * self._roulette_positions[position]
                if position == "first 12" and self._landing_number in range(1, 13):
                    position_winnings += (self._roulette_payout[position]) * self._roulette_positions[position]
                if position == "second 12" and self._landing_number in range(13, 25):
                    position_winnings += (self._roulette_payout[position]) * self._roulette_positions[position]
                if position == "third 12" and self._landing_number in range(26, 37):
                    position_winnings += (self._roulette_payout[position]) * self._roulette_positions[position]
                if position == "top 2-1" and self._landing_number in self._top_row:
                    position_winnings += (self._roulette_payout[position]) * self._roulette_positions[position]
                if position == "mid 2-1" and self._landing_number in self._middle_row:
                    position_winnings += (self._roulette_payout[position]) * self._roulette_positions[position]
                if position == "bot 2-1" and self._landing_number in self._bottom_row:
                    position_winnings += (self._roulette_payout[position]) * self._roulette_positions[position]
                if position_winnings > 0:
                    position_winnings += self._roulette_positions[position]
                total_winnings += position_winnings

        return total_winnings

    def reset(self):
        """Reset the game, clearing all bets and spin results."""
        for key in self._roulette_positions:
            self._roulette_positions[key] = 0
        self._num_bets = 0
        self._landing_number = -1
        self._has_spun = False

    def spin(self):
        """Spin the roulette wheel, generating a random landing number."""
        self._landing_number = random.randint(0, 37)
        self._has_spun = True

    def landed_on_color(self):
        """
        Determine the color of the number the ball landed on.

        Returns:
        tuple: The RGB value of the color (red, black, or green for 0).
        """
        if self._landing_number == 0:
            return 0, 255, 0
        if self._landing_number in self._red_numbers:
            return 255, 0, 0
        return 0, 0, 0
