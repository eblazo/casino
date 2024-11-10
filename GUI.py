"""
Gui.py

This module implements a graphical user interface (GUI) for a casino application
using Pygame. The application features three popular casino games: slots, roulette,
and blackjack, providing an interactive experience for users.

Main Features:
- Slot Machine: A visually engaging slot machine game where players can spin
  the reels and win prizes.
- Roulette: A classic roulette game where players can place bets on numbers
  or colors and watch the wheel spin to determine the winner.
- Blackjack: A card game where players aim to beat the dealer by having a
  hand value closer to 21 without exceeding it.

Dependencies:
- Pygame: This module requires Pygame to create the game window and handle
  user input.
- Account: The `Account` class from `account.py` manages user accounts,
  including balance tracking and bet handling.
- Roulette: The `Roulette` class from `Roulette.py` implements the roulette game logic
  and payouts.
- Slots: The `Slots` class from `Slots.py` handles the slot machine game mechanics
  and outcomes.

Usage:
To run the casino app, execute this module. Ensure that Pygame and all
dependencies are installed and configured properly in your Python environment.
"""

import math
import random
import sys
import time
import pygame
from account import Account
from Roulette import Roulette
from Slots import Slots
from BlackJack import Table

# Initialize Pygame
pygame.init()

account = Account()

# Create the window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Casino')

# Creates default colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 50, 160)
GREEN = (40, 119, 91)
RED = (255, 0, 0)
BROWN = (117, 15, 1)
GREEN0 = (0, 255, 0)
GREEN1 = (0, 150, 25)
GREEN2 = (0, 50, 0)
GREEN3 = (0, 25, 0)

# Create font
font = pygame.font.SysFont(None, 48)
title_font = pygame.font.SysFont(None, 96)
small_font = pygame.font.SysFont(None, 36)
info_font = pygame.font.SysFont(None, 26)
slot_font = pygame.font.SysFont(None, 24)

# Menu, Account, Back Buttons
# Create buttons for menu and account screens
_blue_button1 = pygame.Rect(300, 200, 200, 50)
_blue_button2 = pygame.Rect(300, 300, 200, 50)
_blue_button3 = pygame.Rect(300, 400, 200, 50)
# Creates text for menu screen buttons
_menu_button1_text = font.render("Slots", True, WHITE)
_menu_button2_text = font.render("Roulette", True, WHITE)
_menu_button3_text = font.render("Blackjack", True, WHITE)

# Creates text for adding money to account
_add_button1_text = font.render("$20", True, WHITE)
_add_button2_text = font.render("$50", True, WHITE)
_add_button3_text = font.render("$100", True, WHITE)

# Creates back button
_back_button = pygame.Rect(0, 0, 120, 40)
_back_button_text = small_font.render("Back", True, WHITE)

# Create balance button outside the loop
_balance_button = pygame.Rect(680, 0, 120, 40)


def __draw_balance_button(pygame, screen):
    pygame.draw.rect(screen, BLUE, _balance_button)
    screen.blit(_balance_button_text, (_balance_button.x + 30, _balance_button.y + 10))


def __draw_back_button(pygame, screen):
    pygame.draw.rect(screen, BLUE, _back_button)
    screen.blit(_back_button_text, (_back_button.x + 30, _back_button.y + 10))


def __draw_screen_title(name: str):
    _title = font.render(name, True, WHITE)
    screen.blit(_title, (350, 5))  # Position the new message


# Slot Buttons, Methods and instantiation
slots = Slots()
# Create bet button
_bet_button = pygame.Rect(360, 500, 60, 50)
_spin_button = pygame.Rect(460, 500, 100, 50)

_slot1 = pygame.Rect(100, 160, 100, 200)
_slot2 = pygame.Rect(225, 160, 100, 200)
_slot3 = pygame.Rect(350, 160, 100, 200)
_slot4 = pygame.Rect(475, 160, 100, 200)
_slot5 = pygame.Rect(600, 160, 100, 200)

# Sets current screen to menu
_BET_TEXT = ''
_INVALID_BET_MESSAGE = ''
_message_rect = pygame.Rect(200, 450, 400, 50)


def __spin():
    balance_button = pygame.Rect(680, 0, 120, 40)
    pygame.draw.rect(screen, BLUE, balance_button)
    balance_button_text = small_font.render(str(account), True, WHITE)
    screen.blit(balance_button_text, (balance_button.x + 30, balance_button.y + 10))

    slots.player_won = False
    if not slots.spinning:
        slots.spinning = True
    _symbols = ['1', '2', '3', '4', '5', '7']
    _all_outcomes = []

    for _ in range(25):
        _temp_symbols = [random.choice(_symbols) for _ in range(5)]
        pygame.draw.rect(screen, WHITE, _slot1)
        pygame.draw.rect(screen, WHITE, _slot2)
        pygame.draw.rect(screen, WHITE, _slot3)
        pygame.draw.rect(screen, WHITE, _slot4)
        pygame.draw.rect(screen, WHITE, _slot5)

        # Redraw the black borders around the slot areas
        pygame.draw.rect(screen, BLACK, _slot1, 4)
        pygame.draw.rect(screen, BLACK, _slot2, 4)
        pygame.draw.rect(screen, BLACK, _slot3, 4)
        pygame.draw.rect(screen, BLACK, _slot4, 4)
        pygame.draw.rect(screen, BLACK, _slot5, 4)

        # Render the new symbols
        _temp_symbol1 = title_font.render(_temp_symbols[0], True, BLACK)
        _temp_symbol2 = title_font.render(_temp_symbols[1], True, BLACK)
        _temp_symbol3 = title_font.render(_temp_symbols[2], True, BLACK)
        _temp_symbol4 = title_font.render(_temp_symbols[3], True, BLACK)
        _temp_symbol5 = title_font.render(_temp_symbols[4], True, BLACK)

        # Display the symbols inside the respective slots
        screen.blit(_temp_symbol1, (_slot1.x + 30, _slot1.y + 80))
        screen.blit(_temp_symbol2, (_slot2.x + 30, _slot2.y + 80))
        screen.blit(_temp_symbol3, (_slot3.x + 30, _slot3.y + 80))
        screen.blit(_temp_symbol4, (_slot4.x + 30, _slot4.y + 80))
        screen.blit(_temp_symbol5, (_slot5.x + 30, _slot5.y + 80))
        _all_outcomes.append(_temp_symbols)
        pygame.display.update()
        pygame.time.delay(150)
        # print(f'all outcomes: {_all_outcomes}')

    slots.final_symbols = _all_outcomes[-1]
    # print(f'final symbols: {slots.final_symbols}')

    # Check for a win and store the winning indices
    slots.win_slots = slots.check_win(slots.final_symbols)
    if slots.win_slots:
        slots.player_won = True
        print('You win!')
        print(f'Winning indices: {slots.win_slots}')  # Print the indices of winning symbols
        account.deposit(5 * int(_BET_TEXT))
    else:
        slots.player_won = False
        print('No win.')

    pygame.display.update()
    slots.final_symbols_displayed = True
    slots.spinning = False


def __display_final_symbols():
    _winning_color = (255, 215, 0)  # Gold color for winning symbols
    _symbol_color = BLACK  # Default color for non-winning symbols

    if slots.final_symbols_displayed:
        # Loop through each symbol and display it
        for i in range(5):
            # If the current index is a winning index, use the winning color
            if i in slots.win_slots:
                _color = _winning_color
            else:
                _color = _symbol_color

            # Render the symbol with the appropriate color
            _final_symbol = title_font.render(slots.final_symbols[i], True, _color)

            # Display the symbol in its respective slot
            if i == 0:
                screen.blit(_final_symbol, (_slot1.x + 30, _slot1.y + 80))
            elif i == 1:
                screen.blit(_final_symbol, (_slot2.x + 30, _slot2.y + 80))
            elif i == 2:
                screen.blit(_final_symbol, (_slot3.x + 30, _slot3.y + 80))
            elif i == 3:
                screen.blit(_final_symbol, (_slot4.x + 30, _slot4.y + 80))
            elif i == 4:
                screen.blit(_final_symbol, (_slot5.x + 30, _slot5.y + 80))

        if slots.player_won:
            _win_message = title_font.render("You Win!", True, _winning_color)
            screen.blit(_win_message, (250, 50))  # Adjust position as needed
            pygame.display.update()


# Roulette Buttons, Methods, Variables

roulette_game = Roulette()
_button_width, _button_height = 50, 50
_FIRST_ROW_Y = 350
_SECOND_ROW_Y = 400
_THIRD_ROW_Y = 450

_spin_roulette = pygame.Rect(100, 260, 100, 50)
_spin_roulette_text = font.render("Spin", True, WHITE)

_first12 = pygame.Rect(80, 500, 200, _button_height)
_second12 = pygame.Rect(280, 500, 200, _button_height)
_third12 = pygame.Rect(480, 500, 200, _button_height)
_button_1to18 = pygame.Rect(80, 550, _button_width * 2, _button_height)
_even = pygame.Rect(180, 550, _button_width * 2, _button_height)
_red = pygame.Rect(280, 550, _button_width * 2, _button_height)
_black = pygame.Rect(380, 550, _button_width * 2, _button_height)
_odd = pygame.Rect(480, 550, _button_width * 2, _button_height)
_button_19to36 = pygame.Rect(580, 550, _button_width * 2, _button_height)

# Top Row
_button0 = pygame.Rect(30, _FIRST_ROW_Y, _button_width, _button_height * 3)
_button3 = pygame.Rect(80, _FIRST_ROW_Y, _button_width, _button_height)
_button6 = pygame.Rect(130, _FIRST_ROW_Y, _button_width, _button_height)
_button9 = pygame.Rect(180, _FIRST_ROW_Y, _button_width, _button_height)
_button12 = pygame.Rect(230, _FIRST_ROW_Y, _button_width, _button_height)
_button15 = pygame.Rect(280, _FIRST_ROW_Y, _button_width, _button_height)
_button18 = pygame.Rect(330, _FIRST_ROW_Y, _button_width, _button_height)
_button21 = pygame.Rect(380, _FIRST_ROW_Y, _button_width, _button_height)
_button24 = pygame.Rect(430, _FIRST_ROW_Y, _button_width, _button_height)
_button27 = pygame.Rect(480, _FIRST_ROW_Y, _button_width, _button_height)
_button30 = pygame.Rect(530, _FIRST_ROW_Y, _button_width, _button_height)
_button33 = pygame.Rect(580, _FIRST_ROW_Y, _button_width, _button_height)
_button36 = pygame.Rect(630, _FIRST_ROW_Y, _button_width, _button_height)
_top_column_bet = pygame.Rect(680, _FIRST_ROW_Y, 100, _button_height)

# Middle Row
_button2 = pygame.Rect(80, _SECOND_ROW_Y, _button_width, _button_height)
_button5 = pygame.Rect(130, _SECOND_ROW_Y, _button_width, _button_height)
_button8 = pygame.Rect(180, _SECOND_ROW_Y, _button_width, _button_height)
_button11 = pygame.Rect(230, _SECOND_ROW_Y, _button_width, _button_height)
_button14 = pygame.Rect(280, _SECOND_ROW_Y, _button_width, _button_height)
_button17 = pygame.Rect(330, _SECOND_ROW_Y, _button_width, _button_height)
_button20 = pygame.Rect(380, _SECOND_ROW_Y, _button_width, _button_height)
_button23 = pygame.Rect(430, _SECOND_ROW_Y, _button_width, _button_height)
_button26 = pygame.Rect(480, _SECOND_ROW_Y, _button_width, _button_height)
_button29 = pygame.Rect(530, _SECOND_ROW_Y, _button_width, _button_height)
_button32 = pygame.Rect(580, _SECOND_ROW_Y, _button_width, _button_height)
_button35 = pygame.Rect(630, _SECOND_ROW_Y, _button_width, _button_height)
_middle_column_bet = pygame.Rect(680, _SECOND_ROW_Y, 100, _button_height)

# Bottom Row
_button1 = pygame.Rect(80, _THIRD_ROW_Y, _button_width, _button_height)
_button4 = pygame.Rect(130, _THIRD_ROW_Y, _button_width, _button_height)
_button7 = pygame.Rect(180, _THIRD_ROW_Y, _button_width, _button_height)
_button10 = pygame.Rect(230, _THIRD_ROW_Y, _button_width, _button_height)
_button13 = pygame.Rect(280, _THIRD_ROW_Y, _button_width, _button_height)
_button16 = pygame.Rect(330, _THIRD_ROW_Y, _button_width, _button_height)
_button19 = pygame.Rect(380, _THIRD_ROW_Y, _button_width, _button_height)
_button22 = pygame.Rect(430, _THIRD_ROW_Y, _button_width, _button_height)
_button25 = pygame.Rect(480, _THIRD_ROW_Y, _button_width, _button_height)
_button28 = pygame.Rect(530, _THIRD_ROW_Y, _button_width, _button_height)
_button31 = pygame.Rect(580, _THIRD_ROW_Y, _button_width, _button_height)
_button34 = pygame.Rect(630, _THIRD_ROW_Y, _button_width, _button_height)
_bottom_column_bet = pygame.Rect(680, _THIRD_ROW_Y, 100, 50)

# Puts labels on button
# Out of Board Bets
_first12_text = font.render("First 12", True, WHITE)
_second12_text = font.render("Second 12", True, WHITE)
_third12_text = font.render("Third 12", True, WHITE)
_button_1to18_text = small_font.render("1 to 18", True, WHITE)
_button_19to36_text = small_font.render("19 to 36", True, WHITE)
_even_text = font.render("Even", True, WHITE)
_odd_text = font.render("Odd", True, WHITE)
_red_text = font.render("Red", True, WHITE)
_black_text = font.render("Black", True, WHITE)

# Top Row
_button0_text = font.render("0", True, BLACK)
_button3_text = font.render("3", True, WHITE)
_button6_text = font.render("6", True, WHITE)
_button9_text = font.render("9", True, WHITE)
_button12_text = font.render("12", True, WHITE)
_button15_text = font.render("15", True, WHITE)
_button18_text = font.render("18", True, WHITE)
_button21_text = font.render("21", True, WHITE)
_button24_text = font.render("24", True, WHITE)
_button27_text = font.render("27", True, WHITE)
_button30_text = font.render("30", True, WHITE)
_button33_text = font.render("33", True, WHITE)
_button36_text = font.render("36", True, WHITE)
_top_column_text = small_font.render("2 for 1", True, WHITE)

# Middle Row
_button2_text = font.render("2", True, WHITE)
_button5_text = font.render("5", True, WHITE)
_button8_text = font.render("8", True, WHITE)
_button11_text = font.render("11", True, WHITE)
_button14_text = font.render("14", True, WHITE)
_button17_text = font.render("17", True, WHITE)
_button20_text = font.render("20", True, WHITE)
_button23_text = font.render("23", True, WHITE)
_button26_text = font.render("26", True, WHITE)
_button29_text = font.render("29", True, WHITE)
_button32_text = font.render("32", True, WHITE)
_button35_text = font.render("35", True, WHITE)
_middle_column_text = small_font.render("2 for 1", True, WHITE)

# Bottom Row
_button1_text = font.render("1", True, WHITE)
_button4_text = font.render("4", True, WHITE)
_button7_text = font.render("7", True, WHITE)
_button10_text = font.render("10", True, WHITE)
_button13_text = font.render("13", True, WHITE)
_button16_text = font.render("16", True, WHITE)
_button19_text = font.render("19", True, WHITE)
_button22_text = font.render("22", True, WHITE)
_button25_text = font.render("25", True, WHITE)
_button28_text = font.render("28", True, WHITE)
_button31_text = font.render("31", True, WHITE)
_button34_text = font.render("34", True, WHITE)
_bottom_column_text = small_font.render("2 for 1", True, WHITE)


def __draw_roulette_table_text(screen):
    # Off Board Bets Text
    screen.blit(_first12_text, (_first12.x + 40, _first12.y + 10))
    screen.blit(_second12_text, (_second12.x + 20, _second12.y + 10))
    screen.blit(_third12_text, (_third12.x + 35, _third12.y + 10))
    screen.blit(_button_1to18_text, (_button_1to18.x + 10, _button_1to18.y + 15))
    screen.blit(_button_19to36_text, (_button_19to36.x + 5, _button_19to36.y + 15))
    screen.blit(_even_text, (_even.x + 7, _even.y + 15))
    screen.blit(_odd_text, (_odd.x + 15, _odd.y + 15))
    screen.blit(_red_text, (_red.x + 15, _red.y + 15))
    screen.blit(_black_text, (_black.x + 7, _black.y + 15))
    screen.blit(_button0_text, (_button0.x + 20, _button3.y + 65))

    # Top Row Text
    screen.blit(_button3_text, (_button3.x + 20, _button3.y + 15))
    screen.blit(_button6_text, (_button6.x + 20, _button6.y + 15))
    screen.blit(_button9_text, (_button9.x + 20, _button9.y + 15))
    screen.blit(_button12_text, (_button12.x + 7, _button12.y + 15))
    screen.blit(_button15_text, (_button15.x + 7, _button15.y + 15))
    screen.blit(_button18_text, (_button18.x + 7, _button18.y + 15))
    screen.blit(_button21_text, (_button21.x + 7, _button21.y + 15))
    screen.blit(_button24_text, (_button24.x + 7, _button24.y + 15))
    screen.blit(_button27_text, (_button27.x + 7, _button27.y + 15))
    screen.blit(_button30_text, (_button30.x + 7, _button30.y + 15))
    screen.blit(_button33_text, (_button33.x + 7, _button33.y + 15))
    screen.blit(_button36_text, (_button36.x + 7, _button36.y + 15))
    screen.blit(_top_column_text, (_top_column_bet.x + 15, _top_column_bet.y + 15))

    # Middle Row Text
    screen.blit(_button2_text, (_button2.x + 20, _button2.y + 15))
    screen.blit(_button5_text, (_button5.x + 20, _button5.y + 15))
    screen.blit(_button8_text, (_button8.x + 20, _button8.y + 15))
    screen.blit(_button11_text, (_button11.x + 7, _button11.y + 15))
    screen.blit(_button14_text, (_button14.x + 7, _button14.y + 15))
    screen.blit(_button17_text, (_button17.x + 7, _button17.y + 15))
    screen.blit(_button20_text, (_button20.x + 7, _button20.y + 15))
    screen.blit(_button23_text, (_button23.x + 7, _button23.y + 15))
    screen.blit(_button26_text, (_button26.x + 7, _button26.y + 15))
    screen.blit(_button29_text, (_button29.x + 7, _button29.y + 15))
    screen.blit(_button32_text, (_button32.x + 7, _button32.y + 15))
    screen.blit(_button35_text, (_button35.x + 7, _button35.y + 15))
    screen.blit(_middle_column_text, (_middle_column_bet.x + 15, _middle_column_bet.y + 15))

    # Bottom Row Text
    screen.blit(_button1_text, (_button1.x + 20, _button1.y + 15))
    screen.blit(_button4_text, (_button4.x + 20, _button4.y + 15))
    screen.blit(_button7_text, (_button7.x + 20, _button7.y + 15))
    screen.blit(_button10_text, (_button10.x + 7, _button10.y + 15))
    screen.blit(_button13_text, (_button13.x + 7, _button13.y + 15))
    screen.blit(_button16_text, (_button16.x + 7, _button16.y + 15))
    screen.blit(_button19_text, (_button19.x + 7, _button19.y + 15))
    screen.blit(_button22_text, (_button22.x + 7, _button22.y + 15))
    screen.blit(_button25_text, (_button25.x + 7, _button25.y + 15))
    screen.blit(_button28_text, (_button28.x + 7, _button28.y + 15))
    screen.blit(_button31_text, (_button31.x + 7, _button31.y + 15))
    screen.blit(_button34_text, (_button34.x + 7, _button34.y + 15))
    screen.blit(_bottom_column_text, (_bottom_column_bet.x + 15, _bottom_column_bet.y + 15))


def __draw_roulette_table_buttons(pygame, screen):
    # Creates buttons for Board
    # Off Board Bets
    pygame.draw.rect(screen, GREEN1, _first12)
    pygame.draw.rect(screen, GREEN2, _second12)
    pygame.draw.rect(screen, GREEN1, _third12)
    pygame.draw.rect(screen, GREEN2, _button_1to18)
    pygame.draw.rect(screen, GREEN3, _button_19to36)
    pygame.draw.rect(screen, GREEN3, _even)
    pygame.draw.rect(screen, GREEN2, _odd)
    pygame.draw.rect(screen, RED, _red)
    pygame.draw.rect(screen, BLACK, _black)
    pygame.draw.rect(screen, GREEN0, _button0)

    # Top Row
    pygame.draw.rect(screen, RED, _button3)
    pygame.draw.rect(screen, BLACK, _button6)
    pygame.draw.rect(screen, RED, _button9)
    pygame.draw.rect(screen, RED, _button12)
    pygame.draw.rect(screen, BLACK, _button15)
    pygame.draw.rect(screen, RED, _button18)
    pygame.draw.rect(screen, RED, _button21)
    pygame.draw.rect(screen, BLACK, _button24)
    pygame.draw.rect(screen, RED, _button27)
    pygame.draw.rect(screen, RED, _button30)
    pygame.draw.rect(screen, BLACK, _button33)
    pygame.draw.rect(screen, RED, _button36)
    pygame.draw.rect(screen, GREEN2, _top_column_bet)

    # Middle Row
    pygame.draw.rect(screen, BLACK, _button2)
    pygame.draw.rect(screen, RED, _button5)
    pygame.draw.rect(screen, BLACK, _button8)
    pygame.draw.rect(screen, BLACK, _button11)
    pygame.draw.rect(screen, RED, _button14)
    pygame.draw.rect(screen, BLACK, _button17)
    pygame.draw.rect(screen, BLACK, _button20)
    pygame.draw.rect(screen, RED, _button23)
    pygame.draw.rect(screen, BLACK, _button26)
    pygame.draw.rect(screen, BLACK, _button29)
    pygame.draw.rect(screen, RED, _button32)
    pygame.draw.rect(screen, BLACK, _button35)
    pygame.draw.rect(screen, GREEN1, _middle_column_bet)

    # Bottom Row
    pygame.draw.rect(screen, RED, _button1)
    pygame.draw.rect(screen, BLACK, _button4)
    pygame.draw.rect(screen, RED, _button7)
    pygame.draw.rect(screen, BLACK, _button10)
    pygame.draw.rect(screen, BLACK, _button13)
    pygame.draw.rect(screen, RED, _button16)
    pygame.draw.rect(screen, RED, _button19)
    pygame.draw.rect(screen, BLACK, _button22)
    pygame.draw.rect(screen, RED, _button25)
    pygame.draw.rect(screen, BLACK, _button28)
    pygame.draw.rect(screen, BLACK, _button31)
    pygame.draw.rect(screen, RED, _button34)
    pygame.draw.rect(screen, GREEN2, _bottom_column_bet)


def __draw_roulette_screen(pygame, screen):
    __draw_roulette_table_buttons(pygame, screen)

    __draw_roulette_table_text(screen)

    __draw_screen_title("Roulette")

    __draw_back_button(pygame, screen)

    __draw_balance_button(pygame, screen)

    # Makes spin button on Roulette screen
    pygame.draw.rect(screen, BLACK, _spin_roulette)
    screen.blit(_spin_roulette_text, (_spin_roulette.x + 10, _spin_roulette.y + 10))

    # Creates info on left side of roulette screen
    _click_message = info_font.render("Click on a spot to place a $5 chip.", True, WHITE)
    screen.blit(_click_message, (15, 50))
    _max_bets_message = info_font.render("You can bet up to 3 chips.", True, WHITE)
    screen.blit(_max_bets_message, (15, 80))

    font.set_underline(True)
    _bets_title = font.render("Bets", True, WHITE)
    screen.blit(_bets_title, (600, 50))
    font.set_underline(False)

    _r_bet_x = 600
    _r_bet_y = 100
    for bet in roulette_game.bets_text():
        _bet_text = small_font.render(bet, True, WHITE)
        screen.blit(_bet_text, (_r_bet_x, _r_bet_y))
        _r_bet_y += 50


def __draw_roulette_wheel(pygame, screen, x, y):
    # Circle radius values
    outer_radius = 150  # Outer circle radius
    inner_radius = 130  # Inner circle radius (where numbers are located)

    # Draw black edge of wheel
    pygame.draw.circle(screen, BLACK, (x, y), outer_radius, 5)

    # Draw brown inside of wheel
    pygame.draw.circle(screen, BROWN, (x, y), inner_radius, 0)
    pygame.draw.circle(screen, BROWN, (x, y), outer_radius - 5, 0)

    number_of_sections = 37
    angle_per_section = 360 / number_of_sections

    # Positions and colors for the numbers
    numbers = list(range(37))  # 0-36
    colors = [RED if i in roulette_game.red_numbers else BLACK if i > 0 else GREEN for i in numbers]

    # Draw each section of the roulette wheel
    for i in range(number_of_sections):
        # Angle for each section
        angle = angle_per_section * i
        end_x = x + int(outer_radius * math.cos(math.radians(angle)))
        end_y = y + int(outer_radius * math.sin(math.radians(angle)))

        # Draw the dividing lines for each section
        pygame.draw.line(screen, WHITE, (x, y), (end_x, end_y), 1)

        # Position the text numbers at the midpoints of each section
        mid_angle = angle + angle_per_section / 2
        text_x = x + int(inner_radius * math.cos(math.radians(mid_angle)))
        text_y = y + int(inner_radius * math.sin(math.radians(mid_angle)))

        # Render number text
        number_text = slot_font.render(str(numbers[i]), True, colors[i])
        screen.blit(number_text, (text_x - 10, text_y - 10))

    pygame.draw.circle(screen, BROWN, (x, y), 20, 0)


def __spin_wheel(pygame, screen, x, y):
    # Circle radius values
    outer_radius = 150
    inner_radius = 130

    number_of_sections = 37
    angle_per_section = 360 / number_of_sections

    # Positions and colors for the numbers
    numbers = list(range(37))  # 0-36
    colors = [RED if i in roulette_game.red_numbers
              else BLACK if i > 0 else GREEN0 for i in numbers]

    # Starting angle
    current_angle = 0
    spin_speed = 10
    deceleration = 0.1

    start_time = time.time()
    spinning = True
    while spinning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spinning = False

        # Fill the screen with GREEN background and draw
        # roulette screen for every frame of animation
        screen.fill(GREEN)
        __draw_roulette_screen(pygame, screen)

        # Draw black edge of wheel
        pygame.draw.circle(screen, BLACK, (x, y), outer_radius, 5)

        # Draw brown inside of wheel
        pygame.draw.circle(screen, BROWN, (x, y), inner_radius, 0)
        pygame.draw.circle(screen, BROWN, (x, y), outer_radius - 5, 0)

        # Update each section's angle as the wheel spins
        for i in range(number_of_sections):
            # Rotates the wheel
            angle = angle_per_section * i + current_angle

            # Calculate the endpoint of the lines that divide sections
            end_x = x + int(outer_radius * math.cos(math.radians(angle)))
            end_y = y + int(outer_radius * math.sin(math.radians(angle)))

            # Draw the dividing lines for each section
            pygame.draw.line(screen, WHITE, (x, y), (end_x, end_y), 1)

            # Position the text numbers at the midpoints of each section
            mid_angle = angle + angle_per_section / 2
            text_x = x + int(inner_radius * math.cos(math.radians(mid_angle)))
            text_y = y + int(inner_radius * math.sin(math.radians(mid_angle)))

            # Render number text
            number_text = slot_font.render(str(numbers[i]), True, colors[i])
            screen.blit(number_text, (text_x - 10, text_y - 10))

        pygame.draw.circle(screen, BROWN, (x, y), 20, 0)

        # Update the current angle to simulate spinning
        current_angle += spin_speed

        # Gradually slow down the spin speed to simulate deceleration
        spin_speed = max(spin_speed - deceleration, 0.1)  # Minimum speed to avoid infinite loops

        # Stops the wheel after 6 seconds of spinning
        if time.time() - start_time >= 5:
            spinning = False

        pygame.display.update()

        # Delay to control the frame rate of the spin
        pygame.time.delay(30)


# Blackjack buttons
blackjack = Table(account)
# Rectangles for action buttons on the right side
_bj_small_bet = pygame.Rect(600, 330, 60, 50)
_bj_medium_bet = pygame.Rect(670, 330, 60, 50)
_bj_large_bet = pygame.Rect(740, 330, 60, 50)

_bj_stand = pygame.Rect(600, 400, 200, 50)
_bj_hit = pygame.Rect(600, 470, 200, 50)
_bj_double = pygame.Rect(600, 540, 200, 50)

# Creates text for blackjack right side action buttons
_small_bet_text = small_font.render("$5", True, BLACK)
_medium_bet_text = small_font.render("$10", True, BLACK)
_large_bet_text = small_font.render("$25", True, BLACK)
_stand_text = font.render("Stand", True, BLACK)
_hit_text = font.render("Hit", True, BLACK)
_double_text = font.render("Double", True, BLACK)


def __draw_blackjack_screen(pygame, screen):
    # if game is None:
    screen.fill(GREEN)
    # Blackjack title at top of screen
    __draw_screen_title("Blackjack")

    # Back button
    __draw_back_button(pygame, screen)

    # Account display / button
    __draw_balance_button(pygame, screen)

    # Dealer title and back of cards
    dealer_title = font.render("Dealer", True, BLACK)
    screen.blit(dealer_title, (120, 100))

    # Your title and back of cards
    You_title = font.render("You", True, BLACK)
    screen.blit(You_title, (120, 310))

    # Makes the three betting buttons
    pygame.draw.rect(screen, WHITE, _bj_small_bet)
    pygame.draw.rect(screen, WHITE, _bj_medium_bet)
    pygame.draw.rect(screen, WHITE, _bj_large_bet)
    pygame.draw.rect(screen, WHITE, _bj_double)

    if blackjack.live_game:
        if blackjack.wager == 5:
            pygame.draw.rect(screen, RED, _bj_small_bet)
            pygame.draw.rect(screen, WHITE, _bj_medium_bet)
            pygame.draw.rect(screen, WHITE, _bj_large_bet)
        elif blackjack.wager == 10:
            pygame.draw.rect(screen, WHITE, _bj_small_bet)
            pygame.draw.rect(screen, RED, _bj_medium_bet)
            pygame.draw.rect(screen, WHITE, _bj_large_bet)
        else:
            pygame.draw.rect(screen, WHITE, _bj_small_bet)
            pygame.draw.rect(screen, WHITE, _bj_medium_bet)
            pygame.draw.rect(screen, RED, _bj_large_bet)

        if blackjack.doubled:
            pygame.draw.rect(screen, RED, _bj_double)
        else:
            pygame.draw.rect(screen, WHITE, _bj_double)

    pygame.draw.rect(screen, WHITE, _bj_stand)
    pygame.draw.rect(screen, WHITE, _bj_hit)
    screen.blit(_small_bet_text, (_bj_small_bet.x + 10, _bj_small_bet.y + 10))
    screen.blit(_medium_bet_text, (_bj_medium_bet.x + 8, _bj_medium_bet.y + 10))
    screen.blit(_large_bet_text, (_bj_large_bet.x + 8, _bj_large_bet.y + 10))
    screen.blit(_stand_text, (_bj_stand.x + 30, _bj_stand.y + 10))
    screen.blit(_hit_text, (_bj_hit.x + 30, _bj_hit.y + 10))
    screen.blit(_double_text, (_bj_double.x + 30, _bj_double.y + 10))


card_font = pygame.font.SysFont("arial", 24)
symbols = {
    'H': "\u2665",
    'D': "\u2666",
    'C': "\u2663",
    'S': "\u2660"}


def __card_text(card: str):
    card_name = card[:-1] + symbols[card[-1]]
    if card[-1] in ['H', 'D']:
        return card_font.render(card_name, True, RED)
    return card_font.render(card_name, True, BLACK)


def __card_symbol(card: str):
    card_name = symbols[card[-1]]
    if card[-1] in ['H', 'D']:
        return card_font.render(card_name, True, RED)
    return card_font.render(card_name, True, BLACK)


CURRENT_SCREEN = 0
# Main loop
RUNNING = True
while RUNNING:
    # Update balance button text every iteration
    _balance_button_text = small_font.render(str(account), True, WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

        # handles mouse clicks on various buttons
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            # Universal back and account button
            if _back_button.collidepoint(mouse_pos):
                CURRENT_SCREEN = 0
            if _balance_button.collidepoint(mouse_pos):
                CURRENT_SCREEN = 4

            # Menu screen button actions
            if CURRENT_SCREEN == 0:
                # Sends the player to the game corresponding to the one they click on
                if _blue_button1.collidepoint(mouse_pos):
                    CURRENT_SCREEN = 1
                elif _blue_button2.collidepoint(mouse_pos):
                    CURRENT_SCREEN = 2
                elif _blue_button3.collidepoint(mouse_pos):
                    CURRENT_SCREEN = 3
                elif _balance_button.collidepoint(mouse_pos):
                    CURRENT_SCREEN = 4

            # Slot machine screen events
            if CURRENT_SCREEN == 1:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        _BET_TEXT = _BET_TEXT[:-1]
                    elif event.unicode.isdigit() and len(_BET_TEXT) < 2:
                        _BET_TEXT += event.unicode

            # Roulette screen events
            if CURRENT_SCREEN == 2:
                if account.balance >= 5:
                    button_to_position = [
                        (_button0, "0"), (_button1, "1"), (_button2, "2"), (_button3, "3"),
                        (_button4, "4"), (_button5, "5"), (_button6, "6"), (_button7, "7"),
                        (_button8, "8"), (_button9, "9"), (_button10, "10"), (_button11, "11"),
                        (_button12, "12"), (_button13, "13"), (_button14, "14"), (_button15, "15"),
                        (_button16, "16"), (_button17, "17"), (_button18, "18"), (_button19, "19"),
                        (_button20, "20"), (_button21, "21"), (_button22, "22"), (_button23, "23"),
                        (_button24, "24"), (_button25, "25"), (_button26, "26"), (_button27, "27"),
                        (_button28, "28"), (_button29, "29"), (_button30, "30"), (_button31, "31"),
                        (_button32, "32"), (_button33, "33"), (_button34, "34"), (_button35, "35"),
                        (_button36, "36"), (_first12, "first 12"), (_second12, "second 12"),
                        (_third12, "third 12"), (_button_1to18, "1-18"), (_even, "even"),
                        (_red, "red"), (_black, "black"), (_odd, "odd"), (_button_19to36, "19-36"),
                        (_top_column_bet, "top 2-1"),
                        (_middle_column_bet, "mid 2-1"), (_bottom_column_bet, "bot 2-1")
                    ]
                    # Checks if each button on the table has been pressed
                    # and bets the position if it has.
                    for button in button_to_position:
                        if button[0].collidepoint(mouse_pos):
                            roulette_game.bet_position(button[1], account)
                            break

                # Initiates the roulette wheel spin
                if _spin_roulette.collidepoint(mouse_pos):
                    if roulette_game.num_bets > 0:
                        roulette_game.spin()

            # Blackjack screen events
            if CURRENT_SCREEN == 3:
                if _bj_small_bet.collidepoint(mouse_pos) and not blackjack.live_game:
                    blackjack.bet(5)
                    blackjack.deal()
                elif _bj_medium_bet.collidepoint(mouse_pos) and not blackjack.live_game:
                    blackjack.bet(10)
                    blackjack.deal()
                elif _bj_large_bet.collidepoint(mouse_pos) and not blackjack.live_game:
                    blackjack.bet(25)
                    blackjack.deal()
                elif _bj_stand.collidepoint(mouse_pos) and blackjack.live_game:
                    blackjack.stand()
                elif _bj_hit.collidepoint(mouse_pos) and blackjack.live_game:
                    blackjack.hit()
                elif _bj_double.collidepoint(mouse_pos) and blackjack.live_game:
                    blackjack.double()

            # Account screen events
            if CURRENT_SCREEN == 4:
                if _blue_button1.collidepoint(mouse_pos):
                    account.deposit(20)
                elif _blue_button2.collidepoint(mouse_pos):
                    account.deposit(50)
                elif _blue_button3.collidepoint(mouse_pos):
                    account.deposit(100)

        # Handles bet amount entered on slot screen
        if CURRENT_SCREEN == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    _BET_TEXT = _BET_TEXT[:-1]
                elif event.unicode.isdigit() and len(_BET_TEXT) < 2:
                    _BET_TEXT += event.unicode

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    # Menu screen
    if CURRENT_SCREEN == 0:
        # Create displayed message
        message = title_font.render("GVSU Casino", True, BLACK)
        # Colors the background
        screen.fill(GREEN)
        # Displays 'GVSU Casino' title
        screen.blit(message, (200, 100))

        # Creates buttons for each game
        pygame.draw.rect(screen, BLUE, _blue_button1)
        pygame.draw.rect(screen, BLUE, _blue_button2)
        pygame.draw.rect(screen, BLUE, _blue_button3)
        screen.blit(_menu_button1_text, (_blue_button1.x + 50, _blue_button1.y + 10))
        screen.blit(_menu_button2_text, (_blue_button2.x + 30, _blue_button2.y + 10))
        screen.blit(_menu_button3_text, (_blue_button3.x + 20, _blue_button3.y + 10))

        # Account display / button
        __draw_balance_button(pygame, screen)

    # Slots screen
    elif CURRENT_SCREEN == 1:
        screen.fill(GREEN)

        # Slots title at top of screen
        __draw_screen_title("Slots")

        # Back button
        __draw_back_button(pygame, screen)

        # Account display / button
        __draw_balance_button(pygame, screen)

        # bet amount rectangle
        pygame.draw.rect(screen, BLUE, _bet_button, 2)
        _text_surface = font.render(_BET_TEXT, True, BLACK)
        screen.blit(_text_surface, (_bet_button.x + 10, _bet_button.y + 10))

        # place bet text
        _place_bet_text = font.render('Place bet: $', True, BLACK)
        screen.blit(_place_bet_text, (_bet_button.x - 190, _bet_button.y + 10))

        # spin button
        pygame.draw.rect(screen, BLUE, _spin_button)
        _spin_button_text = font.render('SPIN', True, WHITE)
        screen.blit(_spin_button_text, (_spin_button.x + 10, _spin_button.y + 10))

        # Draw the rectangles
        pygame.draw.rect(screen, WHITE, _slot1)
        pygame.draw.rect(screen, WHITE, _slot2)
        pygame.draw.rect(screen, WHITE, _slot3)
        pygame.draw.rect(screen, WHITE, _slot4)
        pygame.draw.rect(screen, WHITE, _slot5)

        # Border the rectangles with black
        pygame.draw.rect(screen, BLACK, _slot1, 4)
        pygame.draw.rect(screen, BLACK, _slot2, 4)
        pygame.draw.rect(screen, BLACK, _slot3, 4)
        pygame.draw.rect(screen, BLACK, _slot4, 4)
        pygame.draw.rect(screen, BLACK, _slot5, 4)

        __display_final_symbols()

        # make checks for bet amounts
        if _spin_button.collidepoint(mouse_pos) and mouse_pressed[0]:
            if len(_BET_TEXT) >= 1 and not slots.spinning:
                _INVALID_BET_MESSAGE = ''
                # makes sure bet is not subtracted from balance if bet is above 20
                if 0 < int(_BET_TEXT) <= 20:
                    if int(_BET_TEXT) <= account.balance:
                        _INVALID_BET_MESSAGE = ''
                        account.place_bet(int(_BET_TEXT))
                        if not slots.spinning:
                            __spin()
                        if slots.spinning:
                            slots.spinning = True
                        __display_final_symbols()
                        # pygame.display.update()
                    else:
                        _INVALID_BET_MESSAGE = 'You cannot bet more than you have!'

                else:
                    _INVALID_BET_MESSAGE = 'Bet must be between $1 and $20!'
            else:
                _INVALID_BET_MESSAGE = 'Please make a bet before you can spin!'

        if _INVALID_BET_MESSAGE:
            _message_surface = small_font.render(_INVALID_BET_MESSAGE, True, BLACK)
            screen.blit(_message_surface, _message_rect)

    # Roulette screen
    elif CURRENT_SCREEN == 2:
        screen.fill(GREEN)

        __draw_roulette_screen(pygame, screen)
        __draw_roulette_wheel(pygame, screen, 400, 190)

        if roulette_game.has_spun:
            # Spinning Animation runs
            __spin_wheel(pygame, screen, 400, 190)
            # Displays number that was landed on in the correct color
            landing_number_text_1 = small_font.render("Landed On: ", True, WHITE)
            screen.blit(landing_number_text_1, (25, 150))
            landing_number_text_2 = small_font.render(str(roulette_game.landing_number), True,
                                                      roulette_game.landed_on_color())
            screen.blit(landing_number_text_2, (170, 150))
            pygame.display.flip()

            # Calculates and displays the winnings
            winnings = roulette_game.payout()
            if winnings > 0:
                landing_number_text = small_font.render("You WIN $" + str(winnings), True, WHITE)
                screen.blit(landing_number_text, (25, 180))
                pygame.display.flip()
            else:
                landing_number_text = small_font.render("You Lose", True, WHITE)
                screen.blit(landing_number_text, (25, 180))
                pygame.display.flip()

            # Adds winnings and updates the displayed balance
            account.deposit(winnings)
            __draw_balance_button(pygame, screen)

            time.sleep(4)
            roulette_game.reset()

    # Blackjack screen
    elif CURRENT_SCREEN == 3:
        CARD_WIDTH = 100
        CARD_HEIGHT = 156
        CARD_X = 10
        DEALER_CARD_Y = 140
        PLAYER_CARD_Y = 350

        __draw_blackjack_screen(pygame, screen)

        # Dealers cards back
        pygame.draw.rect(screen, RED, (CARD_X, DEALER_CARD_Y, CARD_WIDTH, CARD_HEIGHT), border_radius=15)
        pygame.draw.rect(screen, RED, (CARD_X + 110, DEALER_CARD_Y, CARD_WIDTH, CARD_HEIGHT), border_radius=15)

        # Your cards back
        pygame.draw.rect(screen, RED, (CARD_X, PLAYER_CARD_Y, CARD_WIDTH, CARD_HEIGHT), border_radius=15)
        pygame.draw.rect(screen, RED, (CARD_X + 110, PLAYER_CARD_Y, CARD_WIDTH, CARD_HEIGHT), border_radius=15)

        if blackjack.live_game:
            __draw_blackjack_screen(pygame, screen)
            # print(blackjack.dealer.hand.cards)
            # Draws the dealers showing card
            card = blackjack.dealer.hand.cards[0]
            pygame.draw.rect(screen, WHITE, (CARD_X, DEALER_CARD_Y, CARD_WIDTH, CARD_HEIGHT), border_radius=15)
            card_text = __card_text(str(card))
            diff = 33 if len(str(card)) == 2 else 38
            screen.blit(card_text, (CARD_X + 7, DEALER_CARD_Y + 4))
            screen.blit(card_text, (CARD_X + CARD_WIDTH - diff, DEALER_CARD_Y + CARD_HEIGHT - 30))
            card_text = __card_symbol(str(card))
            screen.blit(card_text, (CARD_X + 40, DEALER_CARD_Y + 63))

            # Draws the dealers hidden card
            pygame.draw.rect(screen, RED, (CARD_X + 110, DEALER_CARD_Y, CARD_WIDTH, CARD_HEIGHT), border_radius=15)

            for card in blackjack.player.hand.cards:
                # Draws the players two initial cards
                pygame.draw.rect(screen, WHITE, (CARD_X, PLAYER_CARD_Y, CARD_WIDTH, CARD_HEIGHT), border_radius=15)
                card_text = __card_text(str(card))
                diff = 33 if len(str(card)) == 2 else 38
                screen.blit(card_text, (CARD_X + 7, PLAYER_CARD_Y + 4))
                screen.blit(card_text, (CARD_X + CARD_WIDTH - diff, PLAYER_CARD_Y + CARD_HEIGHT - 30))
                card_text = __card_symbol(str(card))
                screen.blit(card_text, (CARD_X + 40, PLAYER_CARD_Y + 63))

                CARD_X += 110

            player_value = blackjack.player.hand.value()
            value_text = small_font.render("Value: " + str(player_value), True, BLACK)
            screen.blit(value_text, (120, 530))

            if player_value > 21:
                blackjack.stand()

            CARD_X = 10
            if blackjack.player_done:
                __draw_blackjack_screen(pygame, screen)

                for card in blackjack.dealer.hand.cards:
                    # Draws all the dealers cards at the end of the hand
                    pygame.draw.rect(screen, WHITE, (CARD_X, DEALER_CARD_Y, CARD_WIDTH, CARD_HEIGHT), border_radius=15)
                    card_text = __card_text(str(card))
                    diff = 30 if len(str(card)) == 2 else 40
                    screen.blit(card_text, (CARD_X + 7, DEALER_CARD_Y + 4))
                    screen.blit(card_text, (CARD_X + CARD_WIDTH - diff, DEALER_CARD_Y + CARD_HEIGHT - 30))
                    card_text = __card_symbol(str(card))
                    screen.blit(card_text, (CARD_X + 40, DEALER_CARD_Y + 63))
                    CARD_X += 110

                CARD_X = 10
                for card in blackjack.player.hand.cards:
                    # Draws all the players cards at the end of the hand
                    pygame.draw.rect(screen, WHITE, (CARD_X, PLAYER_CARD_Y, CARD_WIDTH, CARD_HEIGHT), border_radius=15)
                    card_text = __card_text(str(card))
                    diff = 33 if len(str(card)) == 2 else 38
                    screen.blit(card_text, (CARD_X + 7, PLAYER_CARD_Y + 4))
                    screen.blit(card_text, (CARD_X + CARD_WIDTH - diff, PLAYER_CARD_Y + CARD_HEIGHT - 30))
                    card_text = __card_symbol(str(card))
                    screen.blit(card_text, (CARD_X + 40, PLAYER_CARD_Y + 63))
                    CARD_X += 110

                winnings = blackjack.winnings()
                account.deposit(winnings)

                # Draws win message on screen
                if winnings > 0:
                    # creates you win text
                    bj_win_text = font.render("WIN $" + str(winnings), True, WHITE)
                else:
                    bj_win_text = font.render("LOSE", True, WHITE)
                screen.blit(bj_win_text, (600, 100))

                p_value_text = small_font.render("You: " + str(blackjack.player.hand.value()), True, WHITE)
                d_value_text = small_font.render("Dealer: " + str(blackjack.dealer.hand.value()), True, WHITE)
                screen.blit(d_value_text, (600, 150))
                screen.blit(p_value_text, (600, 200))

                pygame.display.flip()
                time.sleep(5)
                blackjack.reset()





    # Account screen
    elif CURRENT_SCREEN == 4:
        screen.fill(GREEN)
        # Account title at top of screen
        __draw_screen_title("Account")

        # Back button
        __draw_back_button(pygame, screen)

        # Displays Account Balance
        screen.blit(title_font.render(str(account), True, BLACK), (325, 100))

        # Creates buttons for each amount that can be added
        pygame.draw.rect(screen, BLUE, _blue_button1)
        pygame.draw.rect(screen, BLUE, _blue_button2)
        pygame.draw.rect(screen, BLUE, _blue_button3)

        screen.blit(_add_button1_text, (_blue_button1.x + 30, _blue_button1.y + 10))
        screen.blit(_add_button2_text, (_blue_button2.x + 30, _blue_button2.y + 10))
        screen.blit(_add_button3_text, (_blue_button3.x + 30, _blue_button3.y + 10))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
