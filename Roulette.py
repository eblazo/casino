import random
import time
from account import Account


class Roulette:
    roulette_payouts = {
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

    def __init__(self):
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
        self.roulette_positions[position] += 5
        account.roulette_bet()

    def num_bets(self):
        num_bets = 0
        for key in self.roulette_positions:
            if self.roulette_positions[key] > 0:
                num_bets += 1
        return num_bets

    def bets_text(self):
        bet_text = []
        for key in self.roulette_positions:
            if self.roulette_positions[key] > 0:
                bet_text.append(str(key) + ": $" + str(self.roulette_positions[key]))
        return bet_text

    def payout(self, landing_position):
        total_winnings = 0
        for position in self.roulette_positions:
            if landing_position == position:
                total_winnings += (roulette_payout[position] + 1) * self.roulette_positions[position]

        return total_winnings

    def reset(self):
        for key in self.roulette_positions:
            self.roulette_positions[key] = 0


# a = Account()
# r = Roulette()
# r.bet_position("1", a)
# print(r.bets_text())
