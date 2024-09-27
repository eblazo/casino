import random
import time
import os

deck = ["Ah", "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "10h", "Jh", "Qh", "Kh",
        "Ad", "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "10d", "Jd", "Qd", "Kd",
        "Ac", "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "10c", "Jc", "Qc", "Kc",
        "As", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "10s", "Js", "Qs", "Ks"]
card_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
               1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
               1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
               1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_hand = []
sum_dealer_hand = 0
player_hand = []
sum_player_hand = 0
used_cards = []
for i in range(2):
    player_hand.append(random.choice(deck))
    used_cards.append(player_hand[i])
    dealer_hand.append(random.choice(deck))
    used_cards.append(dealer_hand[i])

print(f'{"Dealer ->"}{"|"}{dealer_hand[0]}{"|"}{dealer_hand[1]}{"|"}')
print("")
print("")
print(f'{"Player ->"}{"|"}{player_hand[0]}{"|"}{player_hand[1]}{"|"}')
print("1: Stand  2: Hit  3: Double Down")
choice = int(input())
if choice != 1 or choice != 2 or choice != 3:
    print("Invalid input. Please try again")
    choice = int(input())
elif choice == 1:
    while sum(dealer_hand) < 17:
        dealer_hand.append(random.choice(deck))
