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

    def named(self):
        values = {1: 'Ace',
                  2: '2',
                  3: '3',
                  4: '4',
                  5: '5',
                  6: '6',
                  7: '7',
                  8: '8',
                  9: '9',
                  10: '10',
                  11: 'Jack',
                  12: 'Queen',
                  13: 'King'
                  }

        suits = {1: 'Clubs',
                 2: 'Diamonds',
                 3: 'Hearts',
                 4: 'Spades'
                 }
        if self.face_up:
            return values.get(self.number), suits.get(self.suit)
        return "a faced down card"
