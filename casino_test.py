import unittest
from BlackJack import Table
from account import Account
from Roulette import Roulette


class TestYourClassOrFunction(unittest.TestCase):

    def test_roulette_update_balance(self):
        # Checks that the account balance is updated correctly when the player
        # wins in blackjack.
        # Requirement  7
        r = Roulette()
        a = Account()
        r.bet_position("0", a)
        r._landing_number = "0"
        winnings = r.payout()
        a.deposit(winnings)
        self.assertEqual(a.balance, 275)

    def test_cards_delt_after_bet(self):
        # Checks that the user is dealt two cards after they bet.
        # Requirement 16
        a = Account()
        b = Table(a)
        b.deal()
        self.assertEqual(len(b.player.hand.cards), 2)
        self.assertEqual(len(b.dealer.hand.cards), 2)


if __name__ == '__main__':
    unittest.main()
