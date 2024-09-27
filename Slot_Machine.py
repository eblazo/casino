import random


def slot_machine(money):
    print("Welcome to our Dollar slot!")
    print("Please insert money to play")
    print(f'{"Cash = "}{"$"}{money}')
    press = int(input("Press 1 for $1 bet, 2 for $2 bet, 3 for $3 bet\n"))
    run = False
    if press != 1 and press != 2 and press != 3:
        print("Not an appropriate input. Please try again")
    elif money < press:
        print('Not Enough Money to play')
        print("Please retrieve more money before playing")
    else:
        run = True
        while run:
            int1 = random.randint(0, 9)
            int2 = random.randint(0, 9)
            int3 = random.randint(0, 9)
            for i in range(10):
                print("           ")
            print(f'{"|"}{int1}{"|"}{int2}{"|"}{int3}{"|"}')
            if int1 == int2 == int3 == 7:
                print(f'{"Jackpot!! You win $"}{1000*press}')
                money = money + 1000
            elif (int1 == int2 == 7) or (int3 == int2 == 7) or (int1 == int3 == 7):
                print(f'{"You win $"}{20*press}')
                money = money + (20 * press)
            elif (int1 ==7) or (int2 == 7) or (int3 == 7):
                print(f'{"You win $"}{5*press}')
                money = money + (5 * press)
            else:
                money = money - press
            input_accepted = False
            print(f'{"Cash = "}{"$"}{money}')
            print("Press 1 for $1 bet, 2 for $2 bet, 3 for $3 bet")
            print("press 0 to cash out")
            press = int(input())

            while input_accepted == False:
                if press != 1 and press != 2 and press != 3 and press != 0:
                    print("Not an appropriate input. Please try again")
                    press = int(input())
                elif (press == 1 or 2 or 3) and (press != 0):
                    if money < press:
                        print('Not Enough Money to play')
                        print("Please retrieve more money before playing")
                        input_accepted = True
                        run = False
                    else:
                        input_accepted = True
                        run = True
                elif press == 0:
                    run = False
                    print("Thank you for playing!")
                    break




