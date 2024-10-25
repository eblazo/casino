from random import shuffle
from card import Card


class Player:
    def __init__(self, table):
        self.__cards = []
        self.__score = 0
        self.__table = table

    @property
    def score(self) -> int:
        return self.__score

    def play(self):
        print('player turn')
        while True:
            print(f"player: {self.score}")
            if self.score >= 21:
                break
            self.__table.check_bust()
            decision = input('h or s?')
            if decision == 's':
                break
            elif decision == 'h':
                self.give_card(self.__table.shoe.pop())

            else:
                print('needs to be h or s')

    def give_card(self, card):
        self.__cards.append(card)
        self.__score += card.number

    def clear_cards(self):
        cards = self.__cards
        self.__cards = []
        self.__score = 0
        return cards


class Dealer:
    def __init__(self, table):
        self.__cards = []
        self.__score = 0
        self.__table = table

    @property
    def score(self):
        return self.__score

    def play(self):
        print('dealer turn')

        self.__cards[1].face_up = True
        self.__score += self.__cards[1].number

        while (self.score < 17) and (self.score < self.__table.player_score):
            print(f"dealer: {self.score}")
            self.give_card(self.__table.shoe.pop())
            self.__table.check_bust()
        print(f"dealer: {self.score}")

    def give_card(self, card):
        self.__cards.append(card)
        if card.face_up:
            self.__score += card.number

    def clear_cards(self):
        cards = self.__cards
        self.__cards = []
        self.__score = 0
        return cards


class Table:
    def __init__(self, money):
        self.shoe = []
        # 0 is they lost, 1 is they won, 2 is a tie, -1 is currently undecided
        self.__player_win = -1
        self.__player = Player(self)
        self.__dealer = Dealer(self)
        self.__money = money
        self.__wager = int()

    @property
    def player_score(self) -> int:
        return self.__player.score

    @property
    def player_win(self) -> int:
        return self.__player_win

    @player_win.setter
    def player_win(self, num_code: int):
        if not isinstance(num_code, int):
            raise TypeError('The player_win codes are integers')
        if not num_code not in [-1, 0, 1, 2]:
            raise ValueError('The player_win codes are from -1 to 2')

        self.__player_win = num_code

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, amount):
        if not isinstance(amount, int):
            raise TypeError('Money must be an integer')
        self.__money = amount

    @property
    def wager(self):
        return self.__wager

    @wager.setter
    def wager(self, amount):
        if not isinstance(amount, int):
            raise TypeError('Wager must be an integer')
        if amount <= 0:
            raise ValueError('Wager must be greater than 0')
        self.__wager = amount

    def reshuffle(self):
        for deck in range(0, 5):
            for suit in range(1, 5):
                for number in range(1, 14):
                    self.shoe.append(Card(number, suit))
        shuffle(self.shoe)

    def check_bust(self):
        if self.__dealer.score > 21 and self.__player.score > 21:
            self.player_win = 2
        elif self.__player.score > 21:
            self.player_win = 0
        elif self.__dealer.score > 21:
            self.player_win = 1

        if self.player_win != -1:
            self.distribute_money()

    def distribute_money(self):
        if self.player_win == 0:
            self.__money -= self.wager
        elif self.player_win == 1:
            self.__money += self.wager

        print(self.money)

    def reset(self):
        self.__player.clear_cards()
        self.__dealer.clear_cards()
        self.player_win = -1
        self.reshuffle()

        # Gives the player and dealer two cards. One of the dealers will be face down.
        self.__player.give_card(self.shoe.pop())
        self.__player.give_card(self.shoe.pop())
        self.__dealer.give_card(self.shoe.pop())
        face_down_card = self.shoe.pop()
        face_down_card.face_up = False
        self.__dealer.give_card(face_down_card)

    def play_game(self):
        while True:
            self.reset()
            self.wager = int(input('wager?'))
            self.__player.play()

            if self.player_win == -1:
                self.__dealer.play()

            if self.player_win == -1:
                if self.__player.score > self.__dealer.score:
                    self.player_win = 1
                elif self.__player.score < self.__dealer.score:
                    self.player_win = 0
                else:
                    self.player_win = 2

                self.distribute_money()

            again = input('play again y/n')
            if again == 'y':
                self.play_game()
            elif again == 'n':
                break
            else:
                print('y/n please')


t = Table(100)
t.play_game()
