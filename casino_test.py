import unittest
from BlackJack import Table
from BlackJack import Card
from account import Account
from Roulette import Roulette
from Slots import Slots


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

    def test_roulette_bets_text(self):
        # Checks that the bets_text method returns a list of the pet positions
        # in the correct format.
        r = Roulette()
        a = Account()
        r.bet_position("0", a)
        r.bet_position("4", a)
        r.bet_position("8", a)
        self.assertEqual(r.bets_text(), ['0: $5', '4: $5', '8: $5'])

    def test_account_invalid_bet_message_over_betting(self):
        # Checks that the unvalid bet_message for overbetting is correct.
        a = Account()
        a.place_bet(110)
        self.assertEqual(a.invalid_bet_message, 'You cannot bet more than you have!')

    def test_blackjack_cards_delt_after_bet(self):
        # Checks that the user is dealt two cards after they bet.
        # Requirement 16
        a = Account()
        b = Table(a)
        b.deal()
        self.assertEqual(len(b.player.hand.cards), 2)
        self.assertEqual(len(b.dealer.hand.cards), 2)

    def test_blackjack_hit(self):
        # Checks that the hit method in blackjack gives the player an additional card.
        a = Account()
        b = Table(a)
        b.deal()
        b.hit()
        self.assertEqual(len(b.player.hand.cards), 3)

    def test_blackjack_stand_dealer_hit_without_cards(self):
        # Checks that the dealer will hit until their score is greater than or equal to 16.
        a = Account()
        b = Table(a)
        b.stand()
        self.assertGreaterEqual(b.dealer.hand.value(), 16)

    def test_blackjack__payout_win_natural(self):
        # Checks if the payout is correct if the player wins on a blackjack (natural).
        a = Account()
        b = Table(a)
        b.bet(10)
        b.player.hand.add_card(Card('Hearts', 'A'))
        b.player.hand.add_card(Card('Hearts', 'K'))
        b.dealer.hand.add_card(Card('Hearts', 'K'))
        b.dealer.hand.add_card(Card('Hearts', 'K'))
        self.assertEqual(b.winnings(), 25)

    def test_blackjack_payout_win_on_beating_dealer(self):
        # Checks if the payout is correct if the player wins by having a higher score
        # than the dealer.
        a = Account()
        b = Table(a)
        b.bet(10)
        b.player.hand.add_card(Card('Hearts', 'K'))
        b.player.hand.add_card(Card('Hearts', '6'))
        b.player.hand.add_card(Card('Hearts', '5'))
        b.dealer.hand.add_card(Card('Hearts', '2'))
        b.dealer.hand.add_card(Card('Hearts', '3'))
        self.assertGreaterEqual(b.winnings(), 20)

    def test_blackjack_payout_win_on_dealer_bust(self):
        # Checks if the payout is correct if the player wins by having the dealer bust.
        a = Account()
        b = Table(a)
        b.bet(10)
        b.dealer.hand.add_card(Card('Hearts', 'K'))
        b.dealer.hand.add_card(Card('Hearts', 'K'))
        b.dealer.hand.add_card(Card('Hearts', 'K'))
        self.assertGreaterEqual(b.winnings(), 20)

    def test_blackjack_payout_double_and_win(self):
        # Checks if the payout is correct if the player wins and chose to double down.
        a = Account()
        b = Table(a)
        b.bet(10)
        b.double()
        b.player.hand.add_card(Card('Hearts', '7'))
        b.player.hand.add_card(Card('Hearts', 'A'))
        b.player.hand.add_card(Card('Hearts', '3'))
        self.assertGreaterEqual(b.winnings(), 40)

    def test_blackjack_payout_tie(self):
        # Checks if the payout is correct if the game is a tie.
        a = Account()
        b = Table(a)
        b.bet(10)
        b.player.hand.add_card(Card('Hearts', '9'))
        b.dealer.hand.add_card(Card('Hearts', '9'))
        self.assertGreaterEqual(b.winnings(), 10)

    def test_blackjack_payout_loss_on_bust(self):
        # Checks to make sure if there is no payout on a player bust.
        a = Account()
        b = Table(a)
        b.bet(10)
        b.player.hand.add_card(Card('Hearts', 'K'))
        b.player.hand.add_card(Card('Hearts', 'K'))
        b.player.hand.add_card(Card('Clubs', 'K'))
        b.stand()
        self.assertEqual(b.winnings(), 0)

    def test_blackjack_payout_loss_on_low_score(self):
        # Checks to make sure if there is no payout if the dealer has a
        # higher score than the player.
        a = Account()
        b = Table(a)
        b.bet(10)
        b.player.hand.add_card(Card('Hearts', 'K'))
        b.player.hand.add_card(Card('Hearts', '5'))
        b.dealer.hand.add_card(Card('Clubs', 'K'))
        b.dealer.hand.add_card(Card('Clubs', 'K'))
        self.assertEqual(b.winnings(), 0)

    def test_blackjack_reset(self):
        # Checks to make sure the reset method works correctly.
        a = Account()
        b = Table(a)
        b.bet(10)
        b.deal()
        b.hit()
        b.stand()
        b.winnings()
        b.reset()
        self.assertEqual(len(b.player.hand.cards), 0)
        self.assertEqual(len(b.dealer.hand.cards), 0)
        self.assertFalse(b.doubled)
        self.assertFalse(b.live_game)
        self.assertFalse(b.player_done)

    def test_blackjack_ace_as_eleven(self):
        # Checks to make sure aces count as an 11 when it won't put the score over 21.
        a = Account()
        b = Table(a)
        b.player.hand.add_card(Card('Hearts', 'A'))
        self.assertEqual(b.player.hand.value(), 11)

    def test_blackjack_ace_as_one(self):
        # Checks to make sure aces count as a 1 when it would put the score over 21 if 11.
        a = Account()
        b = Table(a)
        b.player.hand.add_card(Card('Hearts', 'A'))
        b.player.hand.add_card(Card('Hearts', 'K'))
        b.player.hand.add_card(Card('Hearts', 'K'))
        self.assertEqual(b.player.hand.value(), 21)

    def test_blackjack_double_forces_stand(self):
        # Checks to make sure doubling down and then hitting forces the player to stand.
        a = Account()
        b = Table(a)
        b.player.hand.add_card(Card('Hearts', 'A'))
        b.double()
        b.hit()
        self.assertTrue(b.player_done)

    def test_blackjack_player_return_cards(self):
        # Checks to make sure the cards method for player returns a Card type.
        a = Account()
        b = Table(a)
        b.deal()
        self.assertTrue(isinstance(b.player.cards()[0], Card))
        self.assertTrue(isinstance(b.player.cards()[1], Card))


if __name__ == '__main__':
    unittest.main()

