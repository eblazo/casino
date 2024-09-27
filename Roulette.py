import random
import time


class Color:
    RED = "\033[31m"
    GREEN = "\033[32m"
    RESET = "\033[0m"


def roulette(money):
    board = []
    number_list = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'
                   '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'
                   '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36')
    for i in range(0, 37):
        board.append(i)
    red = [1, 3, 5, 7, 9, 12, 14, 16, 18,
           19, 21, 23, 25, 27, 30, 32, 34, 36]
    black = [2, 4, 6, 8, 10, 11, 13, 15, 17,
             20, 22, 24, 26, 28, 29, 31, 33, 35]
    columnA = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
    columnB = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
    columnC = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
    print("Welcome to Roulette!")
    play = True
    while play:
        print("-----------------------------------------------------------------------")
        print(f'{"|  "}{" | "}{Color.RED}{board[3]}{Color.RESET}{" | "}{board[6]}{" | "}{Color.RED}{board[9]}{Color.RESET}'
              f'{" | "}{Color.RED}{board[12]}{Color.RESET}{" | "}{board[15]}{" | "}{Color.RED}{board[18]}{Color.RESET}'
              f'{" | "}{Color.RED}{board[21]}{Color.RESET}{" | "}{board[24]}{" | "}{Color.RED}{board[27]}{Color.RESET}'
              f'{" | "}{Color.RED}{board[30]}{Color.RESET}{" | "}{board[33]}{" | "}{Color.RED}{board[36]}{Color.RESET}'
              f'{" | "}{"2to1 A"}{" |"}')
        print("-----------------------------------------------------------------------")
        print(f'{"| "}{Color.GREEN}{board[0]}{Color.RESET}{" | "}{board[2]}{" | "}{Color.RED}{board[5]}{Color.RESET}{" | "}'
              f'{board[8]}{" | "}{board[11]}{" | "}{Color.RED}{board[14]}{Color.RESET}{" | "}{board[17]}'
              f'{" | "}{board[20]}{" | "}{Color.RED}{board[23]}{Color.RESET}{" | "}{board[26]}'
              f'{" | "}{board[29]}{" | "}{Color.RED}{board[32]}{Color.RESET}{" | "}{board[35]}{" | "}{"2to1 B"}{" |"}')
        print("-----------------------------------------------------------------------")
        print(f'{"|  "}{" | "}{Color.RED}{board[1]}{Color.RESET}{" | "}{board[4]}{" | "}{Color.RED}{board[7]}{Color.RESET}'
              f'{" | "}{board[10]}{" | "}{board[13]}{" | "}{Color.RED}{board[16]}{Color.RESET}'
              f'{" | "}{Color.RED}{board[19]}{Color.RESET}{" | "}{board[22]}{" | "}{Color.RED}{board[25]}{Color.RESET}'
              f'{" | "}{board[28]}{" | "}{board[31]}{" | "}{Color.RED}{board[34]}{Color.RESET}{" | "}{"2to1 C"}{" |"}')
        print("-----------------------------------------------------------------------")
        print("|      First 12      |      Second 12    |      Third 12     |")
        print("--------------------------------------------------------------")
        print(f'{"|  1 to 18  |  Even  |  "}{Color.RED}{"Red"}{Color.RESET}{"  |   Black   |  Odd  |  19 to 36 |"}')
        print("--------------------------------------------------------------")
        print("")
        print(f'{"Money = $"}{money}')
        bet = []
        bet_location = []
        winnings = 0
        print("Please place your bets")
        bet_done = False
        while not bet_done:
            bet.append(int(input("Amount -> $")))
            bet_location.append(input("Location -> "))
            answer = input("Would you like to place another bet? (yes or no) -> ")
            if answer == "yes":
                bet_done = False
            elif answer == "no":
                bet_done = True

        print("No more bets!!")
        print(f'{"Total bet amount = $"}{sum(bet)}')
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        roll = random.randint(0, 37)
        if roll in red:
            print(f'{"The number is "}{Color.RED}{roll}{Color.RESET}')
        elif roll == 0:
            print(f'{"The number is "}{Color.GREEN}{roll}{Color.RESET}')
        else:
            print(f'{"The number is "}{roll}')
        for i in range(len(bet_location)):
            if bet_location[i] in number_list:
                bet_location[i] = int(bet_location[i])
                if bet_location[i] == roll:
                    money = money + (36 * bet[i])
            if bet_location[i] == "red" and (roll in red):
                winnings = winnings + (2 * bet[i])
            if bet_location[i] == "black" and (roll in black):
                winnings = winnings + (2 * bet[i])
            if bet_location[i] == "even" and ((roll % 2) == 0):
                winnings = winnings + (2 * bet[i])
            if bet_location[i] == "odd" and ((roll % 2) == 1):
                winnings = winnings + (2 * bet[i])
            if bet_location[i] == "First 12" and (roll <= 12):
                winnings = winnings + (3 * bet[i])
            if bet_location[i] == "Second 12" and ((roll >= 13) and (roll <= 24)):
                winnings = winnings + (3 * bet[i])
            if bet_location[i] == "Third 12" and (roll > 24):
                winnings = winnings + (3 * bet[i])
            if bet_location[i] == "1 to 18" and ((roll >= 1) and (roll <= 18)):
                winnings = winnings + (2 * bet[i])
            if bet_location[i] == "19 to 36" and ((roll >= 1) and (roll <= 18)):
                winnings = winnings + (2 * bet[i])
            if bet_location[i] == "2to1 A" and roll in columnA:
                winnings = winnings + (2 * bet[i])
            if bet_location[i] == "2to1 B" and roll in columnB:
                winnings = winnings + (2 * bet[i])
            if bet_location[i] == "2to1 C" and roll in columnC:
                winnings = winnings + (2 * bet[i])
            else:
                money = money - bet[i]
        if winnings > 0:
            print(f'{"You won $"}{winnings}')
            money = money + winnings
        else:
            print("You Lose :(")
        print(f'{"Money = $"}{money}')
        keep_playing = input("Play again? (yes or no) -> ")
        if keep_playing == "yes":
            play = True
        else:
            print("Thank you for playing!")
            play = False






