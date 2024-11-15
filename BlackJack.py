from random import shuffle
import random

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11}


class Card:
    """
    Represents a playing card with a suit and rank.
    """

    def __init__(self, suit, rank):
        """
        Initialize a Card instance.

        Parameters:
        - suit (str): The suit of the card (e.g., 'Hearts', 'Diamonds').
        - rank (str): The rank of the card (e.g., '2', '3', 'A').
        """
        self.suit = suit
        self.rank = rank

    def value(self):
        """
        Get the card's value based on its rank.

        Returns:
        int: The value of the card.
        """
        return VALUES[self.rank]

    def __str__(self):
        """
        Get a string representation of the card.

        Returns:
        str: The card's rank and the first letter of its suit.
        """
        return self.rank + self.suit[0]


class Deck:
    """
    Represents a deck of 52 playing cards.
    """

    def __init__(self):
        """
        Initialize a Deck instance, creating a full deck and shuffling it.
        """
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))
        self.shuffle()

    def shuffle(self):
        """
        Shuffle the deck.
        """
        random.shuffle(self.cards)

    def deal_single_card(self):
        """
        Deal a single card from the deck.

        Returns:
        Card: The top card from the deck.
        """
        return self.cards.pop()


class Hand:
    """
    Represents a hand of cards held by a player.
    """

    def __init__(self):
        """
        Initialize a Hand instance with an empty list of cards.
        """
        self.cards = []

    def add_card(self, card):
        """
        Add a card to the hand.

        Parameters:
        - card (Card): The card to add.
        """
        self.cards.append(card)

    def value(self):
        """
        Calculate the total value of the hand, adjusting for Aces if necessary.

        Returns:
        int: The total value of the hand.
        """
        value = sum(card.value() for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == 'A')
        while value > 21 and aces > 0:
            value -= 10
            aces -= 1
        return value

    def return_cards(self):
        """
        Return all cards from the hand, emptying the hand.
        """
        self.cards = []


class Player:
    """
    Represents a player in the game, with a hand of cards.
    """

    def __init__(self):
        """
        Initialize a Player instance with an empty hand.
        """
        self.__hand = Hand()

    @property
    def hand(self):
        """
        Get the player's hand.

        Returns:
        Hand: The player's hand.
        """
        return self.__hand

    def cards(self):
        """
        Get the cards in the player's hand.

        Returns:
        list: List of cards in the hand.
        """
        return self.__hand.cards


class Table:
    """
    Represents the game table, managing the deck, players, bets, and game state.
    """

    def __init__(self, account):
        """
        Initialize a Table instance.

        Parameters:
        - account: The player's account to manage bets.
        """
        self.__deck = Deck()
        self.__player = Player()
        self.__dealer = Player()
        self.__wager = 0
        self.__account = account
        self.__live_game = False
        self.__player_done = False
        self.__doubled = False

    @property
    def live_game(self):
        """
        Check if a game is currently live.

        Returns:
        bool: True if the game is live, otherwise False.
        """
        return self.__live_game

    @property
    def player_done(self):
        """
        Check if the player has completed their turn.

        Returns:
        bool: True if the player is done, otherwise False.
        """
        return self.__player_done

    @property
    def wager(self):
        """
        Get the current wager amount.

        Returns:
        int: The wager amount.
        """
        return self.__wager

    @property
    def player(self):
        """
        Get the player at the table.

        Returns:
        Player: The player instance.
        """
        return self.__player

    @property
    def dealer(self):
        """
        Get the dealer at the table.

        Returns:
        Player: The dealer instance.
        """
        return self.__dealer

    @property
    def doubled(self):
        """
        Check if the player has doubled their bet.

        Returns:
        bool: True if the bet is doubled, otherwise False.
        """
        return self.__doubled

    def bet(self, amount):
        """
        Place a bet to start a game.

        Parameters:
        - amount (int): The amount to bet.
        """
        self.__wager = amount
        self.__live_game = True
        self.__account.place_bet(self.__wager)

    def deal(self):
        """
        Deal two cards each to the player and dealer.
        """
        for i in range(2):
            self.__player.hand.add_card(self.__deck.deal_single_card())
            self.__dealer.hand.add_card(self.__deck.deal_single_card())

    def stand(self):
        """
        End the player's turn and play out the dealer's hand according to rules.
        """
        self.__player_done = True
        while self.__dealer.hand.value() <= 16 and self.player.hand.value() < 21:
            self.__dealer.hand.add_card(self.__deck.deal_single_card())

    def hit(self):
        """
        Give the player an additional card. If doubled, force a stand.
        """
        self.__player.hand.add_card(self.__deck.deal_single_card())
        if self.doubled:
            self.stand()

    def double(self):
        """
        Double the player's bet if not already doubled.
        """
        if not self.__doubled:
            self.__account.place_bet(self.__wager)
        self.__doubled = True

    def reset(self):
        """
        Reset the game state for a new round.
        """
        self.__player.hand.return_cards()
        self.__dealer.hand.return_cards()
        self.__live_game = False
        self.__deck = Deck()
        self.__player_done = False
        self.__doubled = False

    def winnings(self):
        """
        Calculate the winnings based on the game's outcome.

        Returns:
        int: The amount won or lost based on the game's results.
        """
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
