import random
import time
import math
from account import Account


class Roulette:
    roulette_payout = {
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
    red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

    top_row = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
    middle_row = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
    bottom_row = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]

    def __init__(self):
        self._num_bets = 0
        self._max_bets = 3
        self.has_spun = False
        self.landing_number = -1
        self.roulette_positions = {
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
        if self._num_bets < self._max_bets:
            self.roulette_positions[position] += 5
            account.roulette_bet()
            self._num_bets += 1

    @property
    def num_bets(self):
        return self._num_bets

    @property
    def max_bets(self):
        return self._max_bets

    def bets_text(self):
        bet_text = []
        for key in self.roulette_positions:
            if self.roulette_positions[key] > 0:
                bet_text.append(str(key) + ": $" + str(self.roulette_positions[key]))
        return bet_text

    def payout(self):
        total_winnings = 0
        for position in self.roulette_positions:
            if self.roulette_positions[position] > 0:
                position_winnings = 0
                # Tests if the ball landed on the exact number
                if self.landing_number == position:
                    position_winnings += (self.roulette_payout[position]) * self.roulette_positions[position]
                elif position == "red" and self.landing_number in self.red_numbers:
                    position_winnings += (self.roulette_payout[position]) * self.roulette_positions[position]
                elif position == "black" and self.landing_number in self.black_numbers:
                    position_winnings += (self.roulette_payout[position]) * self.roulette_positions[position]
                elif position == "even" and self.landing_number % 2 == 0:
                    position_winnings += (self.roulette_payout[position]) * self.roulette_positions[position]
                elif position == "odd" and self.landing_number % 2 == 1:
                    position_winnings += (self.roulette_payout[position]) * self.roulette_positions[position]
                elif position == "1-18" and self.landing_number in range(1, 19):
                    position_winnings += (self.roulette_payout[position]) * self.roulette_positions[position]
                elif position == "19-36" and self.landing_number in range(19, 37):
                    position_winnings += (self.roulette_payout[position]) * self.roulette_positions[position]
                elif position == "first 12" and self.landing_number in range(1, 13):
                    position_winnings += (self.roulette_payout[position]) * self.roulette_positions[position]
                elif position == "second 12" and self.landing_number in range(13, 25):
                    position_winnings += (self.roulette_payout[position]) * self.roulette_positions[position]
                elif position == "third 12" and self.landing_number in range(26, 37):
                    position_winnings += (self.roulette_payout[position]) * self.roulette_positions[position]
                elif position == "top 2-1" and self.landing_number in self.top_row:
                    position_winnings += (self.roulette_payout[position]) * self.roulette_positions[position]
                elif position == "mid 2-1" and self.landing_number in self.middle_row:
                    position_winnings += (self.roulette_payout[position]) * self.roulette_positions[position]
                elif position == "bot 2-1" and self.landing_number in self.bottom_row:
                    position_winnings += (self.roulette_payout[position]) * self.roulette_positions[position]
                if position_winnings > 0:
                    position_winnings += self.roulette_positions[position]
                total_winnings += position_winnings

        return total_winnings

    def reset(self):
        for key in self.roulette_positions:
            self.roulette_positions[key] = 0
        self._num_bets = 0
        self.landing_number = -1
        self.has_spun = False

    def spin(self):
        self.landing_number = random.randint(0, 37)
        self.has_spun = True

    def landed_on_color(self):
        if self.landing_number == 0:
            return 0, 255, 0
        elif self.landing_number in self.red_numbers:
            return 255, 0, 0
        else:
            return 0, 0, 0
