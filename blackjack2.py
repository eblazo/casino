from random import shuffle
from card import Card

shoe = []
player_cards = []
dealer_cards = []
p = 'player'
d = 'dealer'


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

    if competitor == p:
        cards = player_cards
    elif competitor == d:
        cards = dealer_cards
    else:
        raise Exception('Arg must be \'player\' or \'dealer\'')

    for card in cards:
        score += card.number

    return score


def hit(player):
    if player == p:
        player_cards.append(shoe.pop())
    elif player == d:
        dealer_cards.append(shoe.pop())
    else:
        raise ValueError('An argument that was not "p" or "d" was passed for hit()')



def player_turn():
    print('player turn')
    decision = 'h'
    while True:
        decision = input('h or s?')
        if decision == 's':
            break
        if decision == 'h':
            hit(p)
            print(f"player: {check_score(p)}")
            check_bust()


def dealer_turn():
    print('dealer turn')
    while check_score(d) < 17:
        hit(d)
        print(f"dealer: {check_score(d)}")
        check_bust()


def check_bust():
    if check_score(p) > 21:
        exit(f'{p} bust!')
    if check_score(d) > 21:
        exit(f'{d} bust!')




# Getting the hand set up
winner = str()
reshuffle()
deal()
show_cards()
print(f"Player Score:{check_score(p)}")
print(f"Dealer Score:{check_score(d)}")
print()
check_bust()

player_turn()
dealer_turn()

if check_score(p) > check_score(d):
    exit(f'{p} wins')
elif check_score(p) < check_score(d):
    exit(f'{d} wins')
else:
    exit('standoff')
