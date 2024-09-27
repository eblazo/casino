from enum import Enum
import Slot_Machine, Roulette

money = 100


class MenuState(Enum):
    MAIN_MENU = 1
    OPTION_1 = 2
    OPTION_2 = 3
    OPTION_3 = 4
    EXIT = 5


def main_menu():
    print("Welcome to GV Casino!")
    print("Please pick a game")
    print("1. Slots")
    print("2. Roulette")
    print("3. BlackJack")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        return MenuState.OPTION_1
    elif choice == '2':
        return MenuState.OPTION_2
    elif choice == '3':
        return MenuState.OPTION_3
    elif choice == '4':
        return MenuState.EXIT
    else:
        print("Invalid choice.")
        return MenuState.MAIN_MENU


def option_1():
    Slot_Machine.slot_machine(money)
    return MenuState.MAIN_MENU


def option_2():
    Roulette.roulette(money)
    return MenuState.MAIN_MENU


def option_3():
    pass


def run_menu():
    current_state = MenuState.MAIN_MENU

    while current_state != MenuState.EXIT:
        if current_state == MenuState.MAIN_MENU:
            current_state = main_menu()
        elif current_state == MenuState.OPTION_1:
            current_state = option_1()
        elif current_state == MenuState.OPTION_2:
            current_state = option_2()


if __name__ == "__main__":
    run_menu()
