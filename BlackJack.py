import random
import time
import os
import math

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
    def __init__(self, owner):
        self.cards = []
        self.owner = owner

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


class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand('Player')
        self.dealer_hand = Hand('Dealer')
        self.game_over = False
        self.winner = None

    def new_hand(self):
        # resets all values for a new hand
        self.deck = Deck()
        self.player_hand.return_cards()
        self.dealer_hand.return_cards()
        self.game_over = False
        self.winner = None

        # Deals two cards to both player and dealer
        for i in range(2):
            self.player_hand.add_card(self.deck.deal_single_card())
            self.dealer_hand.add_card(self.deck.deal_single_card())

        # Checks if either the player or the dealer got a blackjack
        if self.player_hand.is_Blackjack():
            self.winner = "Player"
            self.game_over = True
        elif self.dealer_hand.is_Blackjack():
            self.winner = "Dealer"
            self.game_over = True

    def hit(self):
        self.player_hand.add_card(self.deck.deal_single_card())
        if self.player_hand.is_bust():
            self.winner = "Dealer"
            self.game_over = True
        elif self.player_hand.is_Blackjack():
            self.winner = "Player"
            self.game_over = True

    def stand(self):
        self.dealer_turn()
        self.find_winner()

    def dealer_turn(self):
        while self.dealer_hand.value() < 17:
            self.dealer_hand.add_card(self.deck.deal_single_card())

    def find_winner(self):
        player_value = self.player_hand.value()
        dealer_value = self.player_hand.value()
        if self.dealer_hand.is_bust():
            self.winner = "Player"
        elif dealer_value > player_value:
            self.winner = "Dealer"
        elif player_value > dealer_value:
            self.winner = "Player"
        else:
            self.winner = "Tie"
        self.game_over = True

    def dealer_first_card(self):
        if len(self.dealer_hand.cards) == 0:
            return
        return self.dealer_hand.cards[0]

