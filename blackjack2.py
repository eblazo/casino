from random import shuffle


shoe = []
player_cards = []
dealer_cards = []

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


def reshuffle():
    for deck in range(0, 5):
        for suit in range(1, 5):
            for number in range(1, 14):
                shoe.append(Card(number, suit))
    shuffle(shoe)


def deal():
    player_cards.append(shoe.pop())
    player_cards.append(shoe.pop())
    dealer_cards.append(shoe.pop())
    dealer_cards.append(shoe.pop())
    dealer_cards[0].face_up = False

def show_cards():
    print('your cards')
    for card in player_cards:
        print(card.named())

    print('dealer cards')
    for card in dealer_cards:
        print(card.named())

#Add aces being worth 10 or 1 eventually
def check_score(competitor):
    score = 0

    if competitor == 'player':
        cards = player_cards
    elif competitor == 'dealer':
        cards = dealer_cards
    else:
        raise Exception('Arg must be \'player\' or \'dealer\'')

    for card in cards:
        score += card.number

    return score

def hit(player: bool):
    if player:
        player_cards.append(shoe.pop())
    dealer_cards.append(shoe.pop())

def player_turn():
    print('player turn')
    decision = 'h'
    while True:
        decision = input('h or s?')
        if decision == 's':
            break
        if decision == 'h':
            hit(True)
            show_cards()

            print(f"player: {check_score('player')}")

def dealer_turn():
    print('dealer turn')
    while check_score('dealer') < 17:
        hit(False)
        show_cards()
        check_score('dealer')

def decide_winner():
    pass


# Getting the hand set up
winner = str()
reshuffle()
deal()
show_cards()
print(f"Player Score:{check_score('player')}")
print(f"Player Score:{check_score('dealer')}")

print()
player_turn()
dealer_turn()


"""
while true:
    get the hand set up
    show the cards
    check if someone has lost
    have it be the players turn
        while the last uption was hit
            give them another option
            check if the player has lost or blackjack
            if blackjack
                end their turn
        
    have it be the dealers turn
    payout
"""
