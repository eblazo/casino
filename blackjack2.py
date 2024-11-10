from random import shuffle
from typing import Tuple


class Card:
    def __init__(self, number: int, suit: int, face_up=True):
        self.__number = number
        self.__suit = suit
        self.__face_up = face_up

    @property
    def number(self):
        return self.__number

    @property
    def suit(self):
        return self.__suit

    @property
    def face_up(self):
        return self.__face_up

    @face_up.setter
    def face_up(self, face_up: bool):
        self.__face_up = face_up

    def __str__(self):
        return f"{self.suit}, {self.number}"


class Player:
    def __init__(self, shoe: list[Card]):
        self.__shoe: list[Card] = shoe
        self.__cards: list[Card] = []
        self.__score = 0
        self.__second_cards: list[Card] = []
        self.__second_score = -1

    @property
    def score(self):
        self.__score = self.__calculate_score(self.__cards)
        return self.__score

    @property
    def second_score(self):
        self.__second_score = self.__calculate_score(self.second_cards)
        return self.__second_score

    @property
    def cards(self) -> list[Card]:
        return self.__cards

    @property
    def second_cards(self) -> list[Card]:
        return self.__second_cards

    def play(self) -> tuple[int, int, bool, bool]:
        doubled_first, doubled_second = False, False
        self.__cards.append(self.__shoe.pop())
        self.__cards.append(self.__shoe.pop())

        # For splitting
        if self.cards[0].number == self.cards[1].number:
            split = input("split? y/n")

            if split == 'y':
                self.__second_cards.append(self.__cards.pop())

        while True:
            print(f"player score: {self.score}")
            if self.score > 21:
                print(f"player score: {self.score}")
                break
            decision = input('h or s or d?')
            if decision == 'h':
                self.cards.append(self.__shoe.pop())
            elif decision == 'd':
                self.cards.append(self.__shoe.pop())
                doubled_first = True
                break
            elif decision == 's':
                break
            else:
                print('needs to be h or s')
        print(f"player score: {self.score}")

        if self.second_cards:
            self.__second_score = 0
            while True:
                print("for hand 2")
                print(f"player score for hand 2: {self.second_score}")
                if self.second_score >= 21:
                    break
                decision = input('h or s?')
                if decision == 'h':
                    self.__second_cards.append(self.__shoe.pop())
                if decision == 'd':
                    self.__second_cards.append(self.__shoe.pop())
                    doubled_second = True
                    break
                elif decision == 's':
                    break
                else:
                    print('needs to be h or s')
            print(f"player score: {self.second_score}")

        return self.__score, self.__second_score, doubled_first, doubled_second

    def clear_cards(self):
        cards = self.__cards + self.__second_cards
        self.__cards = []
        self.__second_cards = []
        self.__score = 0
        self.__second_score = -1
        return cards

    @staticmethod
    def __calculate_score(cards: list[Card]) -> int:
        aces = 0
        no_ace_score = 0

        for card in cards:
            if card.number == 1:
                aces += 1

        if aces == 0:
            for card in cards:
                no_ace_score += card.number
            return no_ace_score

        score_with_eleven = 11
        score_with_one = 1
        aces -= 1
        for card in cards:
            if card.number != 1:
                score_with_eleven += card.number
                score_with_one += card.number
            elif aces != 0:
                aces -= 1
                score_with_eleven += 1
                score_with_one += 1

        if score_with_eleven > 21:
            return score_with_one
        else:
            return score_with_eleven


class Dealer:
    def __init__(self, shoe):
        self.__cards: list[Card] = []
        self.__shoe: list[Card] = shoe
        self.__score = 0

    @property
    def score(self) -> int:
        self.__score = self.__calculate_score()
        return self.__score

    @property
    def cards(self) -> list[Card]:
        cards = []
        for card in self.__cards:
            if card.face_up:
                cards.append(card)
        return cards

    def play(self) -> int:
        self.__cards.append(self.__shoe.pop())
        self.__cards.append(self.__shoe.pop())
        self.__cards[1].face_up = False
        print('dealer turn')

        self.__cards[1].face_up = True
        print(f"dealer: {self.score}")

        while self.score < 17:
            self.give_card(self.__shoe.pop())
            print(f"dealer: {self.score}")
        return self.score

    def give_card(self, card):
        self.__cards.append(card)

    def clear_cards(self) -> list[Card]:
        cards = self.__cards
        self.__cards = []
        self.__score = 0
        return cards

    def __calculate_score(self) -> int:
        aces = 0
        no_ace_score = 0

        for card in self.cards:
            if card.number == 1:
                aces += 1

        if aces == 0:
            for card in self.cards:
                no_ace_score += card.number
            return no_ace_score

        score_with_eleven = 11
        score_with_one = 1
        aces -= 1
        for card in self.cards:
            if card.number != 1:
                score_with_eleven += card.number
                score_with_one += card.number
            elif aces != 0:
                aces -= 1
                score_with_eleven += 1
                score_with_one += 1

        if score_with_eleven > 21:
            return score_with_one
        else:
            return score_with_eleven


class Table:
    def __init__(self, money):
        self.__shoe = []
        self.__player = Player(self.__shoe)
        self.__dealer = Dealer(self.__shoe)
        self.__money = money
        self.__wager = int()
        self.split = False

    @property
    def player_score(self) -> int:
        return self.__player.score

    @property
    def shoe(self):
        return self.__shoe

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

    def play_game(self):
        while True:
            self.__player.clear_cards()
            self.__dealer.clear_cards()
            for deck in range(0, 5):
                for suit in range(1, 5):
                    for number in range(1, 14):
                        self.shoe.append(Card(number, suit))
            shuffle(self.shoe)
            while True:
                self.wager = int(input('wager?'))
                self.__money -= self.wager
                # 1 for a win, 0 for a loss, -1 for a tie
                player_wins = [0, 0]

                player_score_1, player_score_2, doubled_first, doubled_second = self.__player.play()

                if player_score_2 > 0:
                    self.split = True
                    self.__money -= self.wager
                if doubled_first:
                    self.__money -= self.wager
                if doubled_second:
                    self.__money -= self.wager

                # if the player busts
                if player_score_1 > 21 and player_score_2 > 21:
                    break
                if player_score_1 > 21 and not self.split:
                    break

                dealer_score = self.__dealer.play()

                # if the dealer busts
                if dealer_score > 21:
                    if not self.split:
                        player_wins[0] = 1
                        break
                    else:
                        if player_score_1 <= 21:
                            player_wins[0] = 1
                        if player_score_2 <= 21:
                            player_wins[1] = 1
                        break

                # If neither bust
                if player_score_1 > dealer_score:
                    player_wins[0] = 1
                elif player_score_1 == dealer_score:
                    player_wins[0] = -1

                if self.split:
                    if player_score_2 > dealer_score:
                        player_wins[1] = 1
                    elif player_score_2 == dealer_score:
                        player_wins[-1] = -1
                    break
                break

            # Distribute money
            if doubled_first and player_wins[0] == 1:
                self.__money += self.wager * 4
            elif doubled_first and player_wins[0] == -1:
                self.__money += self.wager * 2
            elif player_wins[0] == 1:
                self.__money += self.wager * 2
            elif player_wins[0] == -1:
                self.__money += self.wager
            if self.split:
                if doubled_second and player_wins[1] == 1:
                    self.__money += self.wager * 4
                elif doubled_second and player_wins[1] == -1:
                    self.__money += self.wager * 2
                elif player_wins[1] == 1:
                    self.__money += self.wager * 2
                elif player_wins[1] == -1:
                    self.__money += self.wager
            print(f"money: {self.money}")

            again = input('play again y/n')
            if again == 'y':
                self.play_game()
            elif again == 'n':
                exit()
            else:
                print('y/n please')


t = Table(100)
t.play_game()
