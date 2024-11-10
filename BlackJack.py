from random import shuffle
import random

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def value(self):
        return VALUES[self.rank]

    def __str__(self):
        return self.rank + self.suit[0]


class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_single_card(self):
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def value(self):
        value = 0
        for card in self.cards:
            value += card.value()
        aces = 0
        for card in self.cards:
            if card.rank == 'A':
                aces += 1
        while value > 21 and aces > 0:
            value -= 10
            aces -= 1
        return value

    def is_bust(self):
        return self.value() > 21

    def is_Blackjack(self):
        return self.value() == 21

    def return_cards(self):
        self.cards = []


class Player:
    def __init__(self):
        self.__hand = Hand()

    @property
    def hand(self):
        return self.__hand

    def cards(self):
        return self.__hand.cards

    def give_card(self, card):
        self.__cards.append(card)
        self.__score += card.number


class Table:
    def __init__(self, account):
        self.__deck = Deck()
        self.__player = Player()
        self.__dealer = Player()
        self.__wager = 0
        self.__account = account
        self.__live_game = False
        self.__player_done = False
        self.__doubled = False

    @property
    def player_win(self) -> int:
        return self.__player_win

    @property
    def live_game(self):
        return self.__live_game

    @property
    def player_done(self):
        return self.__player_done

    @property
    def wager(self):
        return self.__wager

    @property
    def player(self):
        return self.__player

    @property
    def dealer(self):
        return self.__dealer

    @property
    def doubled(self):
        return self.__doubled

    def bet(self, amount):
        self.__wager = amount
        self.__live_game = True
        self.__account.place_bet(self.__wager)

    def deal(self):
        for i in range(2):
            self.__player.hand.add_card(self.__deck.deal_single_card())
            self.__dealer.hand.add_card(self.__deck.deal_single_card())

    def stand(self):
        self.__player_done = True
        while self.__dealer.hand.value() <= 16 and self.player.hand.value() < 21:
            self.__dealer.hand.add_card(self.__deck.deal_single_card())

    def hit(self):
        self.__player.hand.add_card(self.__deck.deal_single_card())
        if self.doubled:
            self.stand()

    def double(self):
        self.__doubled = True
        self.__account.place_bet(self.__wager)

    def reset(self):
        self.__player.hand.return_cards()
        self.__dealer.hand.return_cards()
        self.__live_game = False
        self.__deck.shuffle()
        self.__deck = Deck()
        self.__player_done = False
        self.__doubled = False

    def winnings(self):
        p_value = self.player.hand.value()
        d_value = self.dealer.hand.value()
        bet_amount = self.wager
        if self.doubled:
            bet_amount *= 2

        if p_value > 21:
            return 0

        elif d_value > 21:
            return bet_amount * 2

        if p_value == 21 and len(self.player.hand.cards) == 2:
            return bet_amount + int(bet_amount * 1.5)

        elif p_value > d_value:
            return bet_amount * 2

        elif p_value == d_value:
            return bet_amount

        return 0
