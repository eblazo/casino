import random
import time


def check_win(symbols):
    for i in range(3):
        if symbols[i] == symbols[i + 1] == symbols[i + 2]:
            return True
    return False


def get_bet_amount():
    while True:
        try:
            bet_amount = int(input('Place bet amount: '))
            if bet_amount <= 0:
                print('You must bet a value greater than $0.')
            elif bet_amount > 20:
                print('Cannot bet over $20. Please try again.')
            else:
                return bet_amount
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def slots(money, bet_amount=None):
    symbols = ['1', '2', '3', '4', '5', '7']
    print(f'{"Money = $"}{money}')

    # Determine the bet amount
    if bet_amount is None:
        bet_amount = get_bet_amount()

    print(f'Amount -> ${bet_amount}')

    # Check if the user wants to quit
    ui = input('Press Enter to spin, "q" to quit, or "change" to change bet amount: ')

    if ui.lower() == 'q':
        print("Thank you for playing!")
        quit()

    if ui.lower() == 'change':
        bet_amount = get_bet_amount()
        print(f'New Amount -> ${bet_amount}')

    # Check if the user can afford the bet
    if (money - bet_amount) < 0:
        print('You cannot bet more than you have!')
        return slots(money, bet_amount)

    # Spin the slots
    final_symbols = [random.choice(symbols) for _ in range(5)]

    # Spin animation
    for _ in range(25):
        temp_output = f'\r{" | ".join([random.choice(symbols) for _ in range(5)])}'
        print(temp_output, end='')
        time.sleep(0.05)

    final_result = ' | '.join(final_symbols)
    print(f'\r{final_result}    ')

    # Check for win
    if check_win(final_symbols):
        print("You won!")
        money += (bet_amount * 5)  # Adjust winnings based on bet
    else:
        print("Try again.")
        money -= bet_amount  # Deduct bet amount if lost

    # Continue the game
    slots(money, bet_amount)  # Pass the current bet amount to the next call


if __name__ == '__main__':
    slots(100)
