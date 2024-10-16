import pygame
import sys
import random
import time
from account import Account
from Roulette import Roulette
from Slots import Slots
# Initialize Pygame
pygame.init()


account = Account()
slots = Slots()

# Set up the window dimensions
width, height = 800, 600

# Create the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Casino')

# Creates default colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 50, 160)
GREEN = (40, 119, 91)
RED = (255, 0, 0)
GREEN0 = (0, 255, 0)
GREEN1 = (0, 150, 25)
GREEN2 = (0, 50, 0)
GREEN3 = (0, 25, 0)

# Create font
font = pygame.font.SysFont(None, 48)
title_font = pygame.font.SysFont(None, 96)
small_font = pygame.font.SysFont(None, 36)
"""
Menu, Account, Back Buttons
"""
# Create displayed message
message = title_font.render("GVSU Casino", True, BLACK)
# Create buttons for menu and account screens
button_width, button_height = 200, 50
blue_button1 = pygame.Rect(300, 200, button_width, button_height)
blue_button2 = pygame.Rect(300, 300, button_width, button_height)
blue_button3 = pygame.Rect(300, 400, button_width, button_height)
# Creates text for menu screen buttons
menu_button1_text = font.render("Slots", True, WHITE)
menu_button2_text = font.render("Roulette", True, WHITE)
menu_button3_text = font.render("Blackjack", True, WHITE)

# Creates text for adding money to account
add_button1_text = font.render("$20", True, WHITE)
add_button2_text = font.render("$50", True, WHITE)
add_button3_text = font.render("$100", True, WHITE)

# Creates back button
back_button = pygame.Rect(0, 0, 120, 40)
back_button_text = small_font.render("Back", True, WHITE)

"""
Slot Buttons and instantiation 
"""
# Create bet button
bet_button = pygame.Rect(360, 500, 60, 50)
spin_button = pygame.Rect(460, 500, 100, 50)

# Sets current screen to menu
bet_text = ''
invalid_bet_message = ''
message_rect = pygame.Rect(200, 450, 400, 50)

# Create balance button outside the loop
balance_button = pygame.Rect(680, 0, 120, 40)

"""
Roulette Buttons and instantiation
"""
button_width, button_height = 50, 50
column_bet_width, column_bet_height = 100, 50
three12_width, three12_height = 200, 50
other_bets_width, other_bets_height = 100, 50
first_row_y = 350
second_row_y = 400
third_row_y = 450

first12 = pygame.Rect(80, 500, three12_width, three12_height)
second12 = pygame.Rect(280, 500, three12_width, three12_height)
third12 = pygame.Rect(480, 500, three12_width, three12_height)
button_1to18 = pygame.Rect(80, 550, other_bets_width, button_height)
even = pygame.Rect(180, 550, other_bets_width, other_bets_height)
red = pygame.Rect(280, 550, other_bets_width, other_bets_height)
black = pygame.Rect(380, 550, other_bets_width, other_bets_height)
odd = pygame.Rect(480, 550, other_bets_width, other_bets_height)
button_19to36 = pygame.Rect(580, 550, other_bets_width, other_bets_height)

# Top Row
button0 = pygame.Rect(30, first_row_y, button_width, button_height * 3)
button3 = pygame.Rect(80, first_row_y, button_width, button_height)
button6 = pygame.Rect(130, first_row_y, button_width, button_height)
button9 = pygame.Rect(180, first_row_y, button_width, button_height)
button12 = pygame.Rect(230, first_row_y, button_width, button_height)
button15 = pygame.Rect(280, first_row_y, button_width, button_height)
button18 = pygame.Rect(330, first_row_y, button_width, button_height)
button21 = pygame.Rect(380, first_row_y, button_width, button_height)
button24 = pygame.Rect(430, first_row_y, button_width, button_height)
button27 = pygame.Rect(480, first_row_y, button_width, button_height)
button30 = pygame.Rect(530, first_row_y, button_width, button_height)
button33 = pygame.Rect(580, first_row_y, button_width, button_height)
button36 = pygame.Rect(630, first_row_y, button_width, button_height)
top_column_bet = pygame.Rect(680, first_row_y, column_bet_width, column_bet_height)

# Middle Row
button2 = pygame.Rect(80, second_row_y, button_width, button_height)
button5 = pygame.Rect(130, second_row_y, button_width, button_height)
button8 = pygame.Rect(180, second_row_y, button_width, button_height)
button11 = pygame.Rect(230, second_row_y, button_width, button_height)
button14 = pygame.Rect(280, second_row_y, button_width, button_height)
button17 = pygame.Rect(330, second_row_y, button_width, button_height)
button20 = pygame.Rect(380, second_row_y, button_width, button_height)
button23 = pygame.Rect(430, second_row_y, button_width, button_height)
button26 = pygame.Rect(480, second_row_y, button_width, button_height)
button29 = pygame.Rect(530, second_row_y, button_width, button_height)
button32 = pygame.Rect(580, second_row_y, button_width, button_height)
button35 = pygame.Rect(630, second_row_y, button_width, button_height)
middle_column_bet = pygame.Rect(680, second_row_y, column_bet_width, column_bet_height)

# Bottom Row
button1 = pygame.Rect(80, third_row_y, button_width, button_height)
button4 = pygame.Rect(130, third_row_y, button_width, button_height)
button7 = pygame.Rect(180, third_row_y, button_width, button_height)
button10 = pygame.Rect(230, third_row_y, button_width, button_height)
button13 = pygame.Rect(280, third_row_y, button_width, button_height)
button16 = pygame.Rect(330, third_row_y, button_width, button_height)
button19 = pygame.Rect(380, third_row_y, button_width, button_height)
button22 = pygame.Rect(430, third_row_y, button_width, button_height)
button25 = pygame.Rect(480, third_row_y, button_width, button_height)
button28 = pygame.Rect(530, third_row_y, button_width, button_height)
button31 = pygame.Rect(580, third_row_y, button_width, button_height)
button34 = pygame.Rect(630, third_row_y, button_width, button_height)
bottom_column_bet = pygame.Rect(680, third_row_y, column_bet_width, column_bet_height)

# Puts labels on button
# Out of Board Bets
first12_text = font.render("First 12", True, WHITE)
second12_text = font.render("Second 12", True, WHITE)
third12_text = font.render("Third 12", True, WHITE)
button_1to18_text = small_font.render("1 to 18", True, WHITE)
button_19to36_text = small_font.render("19 to 36", True, WHITE)
even_text = font.render("Even", True, WHITE)
odd_text = font.render("Odd", True, WHITE)
red_text = font.render("Red", True, WHITE)
black_text = font.render("Black", True, WHITE)

# Top Row
button0_text = font.render("0", True, BLACK)
button3_text = font.render("3", True, WHITE)
button6_text = font.render("6", True, WHITE)
button9_text = font.render("9", True, WHITE)
button12_text = font.render("12", True, WHITE)
button15_text = font.render("15", True, WHITE)
button18_text = font.render("18", True, WHITE)
button21_text = font.render("21", True, WHITE)
button24_text = font.render("24", True, WHITE)
button27_text = font.render("27", True, WHITE)
button30_text = font.render("30", True, WHITE)
button33_text = font.render("33", True, WHITE)
button36_text = font.render("36", True, WHITE)
top_column_text = small_font.render("2 for 1", True, WHITE)

# Middle Row
button2_text = font.render("2", True, WHITE)
button5_text = font.render("5", True, WHITE)
button8_text = font.render("8", True, WHITE)
button11_text = font.render("11", True, WHITE)
button14_text = font.render("14", True, WHITE)
button17_text = font.render("17", True, WHITE)
button20_text = font.render("20", True, WHITE)
button23_text = font.render("23", True, WHITE)
button26_text = font.render("26", True, WHITE)
button29_text = font.render("29", True, WHITE)
button32_text = font.render("32", True, WHITE)
button35_text = font.render("35", True, WHITE)
middle_column_text = small_font.render("2 for 1", True, WHITE)

# Bottom Row
button1_text = font.render("1", True, WHITE)
button4_text = font.render("4", True, WHITE)
button7_text = font.render("7", True, WHITE)
button10_text = font.render("10", True, WHITE)
button13_text = font.render("13", True, WHITE)
button16_text = font.render("16", True, WHITE)
button19_text = font.render("19", True, WHITE)
button22_text = font.render("22", True, WHITE)
button25_text = font.render("25", True, WHITE)
button28_text = font.render("28", True, WHITE)
button31_text = font.render("31", True, WHITE)
button34_text = font.render("34", True, WHITE)
bottom_column_text = small_font.render("2 for 1", True, WHITE)
roulette_game = Roulette()

"""
Blackjack buttons
"""
# Rectangles for action buttons on the right side
button_width, button_height = 200, 50
bj_small_bet = pygame.Rect(600, 330, 60, button_height)
bj_medium_bet = pygame.Rect(670, 330, 60, button_height)
bj_large_bet = pygame.Rect(740, 330, 60, button_height)

bj_stand = pygame.Rect(600, 400, button_width, button_height)
bj_hit = pygame.Rect(600, 470, button_width, button_height)
bj_double = pygame.Rect(600, 540, button_width, button_height)

# Creates text for blackjack right side action buttons
small_bet_text = small_font.render("$5", True, BLACK)
medium_bet_text = small_font.render("$10", True, BLACK)
large_bet_text = small_font.render("$25", True, BLACK)
stand_text = font.render("Stand", True, BLACK)
hit_text = font.render("Hit", True, BLACK)
double_text = font.render("Double", True, BLACK)
roulette_bet_position = None

current_screen = 0

'''
Create spin function for slot game
'''
def spin():
    slots.player_won = False
    if not slots.spinning:
        slots.spinning = True
    symbols = ['1', '2', '3', '4', '5', '7']
    all_outcomes = []

    for _ in range(25):
        temp_symbols = [random.choice(symbols) for _ in range(5)]
        pygame.draw.rect(screen, WHITE, slot1)
        pygame.draw.rect(screen, WHITE, slot2)
        pygame.draw.rect(screen, WHITE, slot3)
        pygame.draw.rect(screen, WHITE, slot4)
        pygame.draw.rect(screen, WHITE, slot5)

        # Redraw the black borders around the slot areas
        pygame.draw.rect(screen, BLACK, slot1, 4)
        pygame.draw.rect(screen, BLACK, slot2, 4)
        pygame.draw.rect(screen, BLACK, slot3, 4)
        pygame.draw.rect(screen, BLACK, slot4, 4)
        pygame.draw.rect(screen, BLACK, slot5, 4)

        # Render the new symbols
        temp_symbol1 = title_font.render(temp_symbols[0], True, BLACK)
        temp_symbol2 = title_font.render(temp_symbols[1], True, BLACK)
        temp_symbol3 = title_font.render(temp_symbols[2], True, BLACK)
        temp_symbol4 = title_font.render(temp_symbols[3], True, BLACK)
        temp_symbol5 = title_font.render(temp_symbols[4], True, BLACK)

        # Display the symbols inside the respective slots
        screen.blit(temp_symbol1, (slot1.x + 30, slot1.y + 80))
        screen.blit(temp_symbol2, (slot2.x + 30, slot2.y + 80))
        screen.blit(temp_symbol3, (slot3.x + 30, slot3.y + 80))
        screen.blit(temp_symbol4, (slot4.x + 30, slot4.y + 80))
        screen.blit(temp_symbol5, (slot5.x + 30, slot5.y + 80))
        all_outcomes.append(temp_symbols)
        pygame.display.update()
        pygame.time.delay(150)
        print(f'all outcomes: {all_outcomes}')

    slots.final_symbols = all_outcomes[-1]
    print(f'final symbols: {slots.final_symbols}')

    # Check for a win and store the winning indices
    slots.win_slots = slots.check_win(slots.final_symbols)
    if slots.win_slots:
        player_won = True
        print('You win!')
        print(f'Winning indices: {slots.win_slots}')  # Print the indices of winning symbols
    else:
        player_won = False
        print('No win.')

    pygame.display.update()
    slots.final_symbols_displayed = True
    slots.spinning = False

'''
Create function to display symbols of slot game
'''

def display_final_symbols():
    winning_color = (255, 215, 0)  # Gold color for winning symbols
    symbol_color = BLACK  # Default color for non-winning symbols

    if slots.final_symbols_displayed:
        # Loop through each symbol and display it
        for i in range(5):
            # If the current index is a winning index, use the winning color
            if i in slots.win_slots:
                color = winning_color
            else:
                color = symbol_color

            # Render the symbol with the appropriate color
            final_symbol = title_font.render(slots.final_symbols[i], True, color)

            # Display the symbol in its respective slot
            if i == 0:
                screen.blit(final_symbol, (slot1.x + 30, slot1.y + 80))
            elif i == 1:
                screen.blit(final_symbol, (slot2.x + 30, slot2.y + 80))
            elif i == 2:
                screen.blit(final_symbol, (slot3.x + 30, slot3.y + 80))
            elif i == 3:
                screen.blit(final_symbol, (slot4.x + 30, slot4.y + 80))
            elif i == 4:
                screen.blit(final_symbol, (slot5.x + 30, slot5.y + 80))

        if slots.player_won:
            win_message = title_font.render("You Win!", True, winning_color)
            screen.blit(win_message, (250, 50))  # Adjust position as needed
            pygame.display.update()




# Main loop
running = True
while running:
    # Update balance button text every iteration
    balance_button_text = small_font.render(str(account), True, WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # handles mouse clicks on various buttons
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            # Universal back and account button
            if back_button.collidepoint(mouse_pos):
                current_screen = 0
            if balance_button.collidepoint(mouse_pos):
                current_screen = 4

            '''
            # Slot machine screen events
            if current_screen == 1:
                if spin_button.collidepoint(mouse_pos):
                    # makes sure bet is not subtracted from balance if bet is above 20
                    if 0 < int(bet_text) <= 20:
                        account.place_bet(int(bet_text))
            '''
            if current_screen == 1:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        bet_text = bet_text[:-1]
                    elif event.unicode.isdigit() and len(bet_text) < 2:
                        bet_text += event.unicode

            # Roulette screen events
            if current_screen == 2:
                if account.balance >= 5:
                    if button0.collidepoint(mouse_pos):
                        roulette_game.bet_position("0", account)
                    elif button1.collidepoint(mouse_pos):
                        roulette_game.bet_position("1", account)
                    elif button2.collidepoint(mouse_pos):
                        roulette_game.bet_position("2", account)
                    elif button3.collidepoint(mouse_pos):
                        roulette_game.bet_position("3", account)
                    elif button4.collidepoint(mouse_pos):
                        roulette_game.bet_position("4", account)
                    elif button5.collidepoint(mouse_pos):
                        roulette_game.bet_position("5", account)
                    elif button6.collidepoint(mouse_pos):
                        roulette_game.bet_position("6", account)
                    elif button7.collidepoint(mouse_pos):
                        roulette_game.bet_position("7", account)
                    elif button8.collidepoint(mouse_pos):
                        roulette_game.bet_position("8", account)
                    elif button9.collidepoint(mouse_pos):
                        roulette_game.bet_position("9", account)
                    elif button10.collidepoint(mouse_pos):
                        roulette_game.bet_position("10", account)
                    elif button11.collidepoint(mouse_pos):
                        roulette_game.bet_position("11", account)
                    elif button12.collidepoint(mouse_pos):
                        roulette_game.bet_position("12", account)
                    elif button13.collidepoint(mouse_pos):
                        roulette_game.bet_position("13", account)
                    elif button14.collidepoint(mouse_pos):
                        roulette_game.bet_position("14", account)
                    elif button15.collidepoint(mouse_pos):
                        roulette_game.bet_position("15", account)
                    elif button16.collidepoint(mouse_pos):
                        roulette_game.bet_position("16", account)
                    elif button17.collidepoint(mouse_pos):
                        roulette_game.bet_position("17", account)
                    elif button18.collidepoint(mouse_pos):
                        roulette_game.bet_position("18", account)
                    elif button19.collidepoint(mouse_pos):
                        roulette_game.bet_position("19", account)
                    elif button20.collidepoint(mouse_pos):
                        roulette_game.bet_position("20", account)
                    elif button21.collidepoint(mouse_pos):
                        roulette_game.bet_position("21", account)
                    elif button22.collidepoint(mouse_pos):
                        roulette_game.bet_position("22", account)
                    elif button23.collidepoint(mouse_pos):
                        roulette_game.bet_position("23", account)
                    elif button24.collidepoint(mouse_pos):
                        roulette_game.bet_position("24", account)
                    elif button25.collidepoint(mouse_pos):
                        roulette_game.bet_position("25", account)
                    elif button26.collidepoint(mouse_pos):
                        roulette_game.bet_position("26", account)
                    elif button27.collidepoint(mouse_pos):
                        roulette_game.bet_position("27", account)
                    elif button28.collidepoint(mouse_pos):
                        roulette_game.bet_position("28", account)
                    elif button29.collidepoint(mouse_pos):
                        roulette_game.bet_position("29", account)
                    elif button30.collidepoint(mouse_pos):
                        roulette_game.bet_position("30", account)
                    elif button31.collidepoint(mouse_pos):
                        roulette_game.bet_position("31", account)
                    elif button32.collidepoint(mouse_pos):
                        roulette_game.bet_position("32", account)
                    elif button33.collidepoint(mouse_pos):
                        roulette_game.bet_position("33", account)
                    elif button34.collidepoint(mouse_pos):
                        roulette_game.bet_position("34", account)
                    elif button35.collidepoint(mouse_pos):
                        roulette_game.bet_position("35", account)
                    elif button36.collidepoint(mouse_pos):
                        roulette_game.bet_position("36", account)
                    elif first12.collidepoint(mouse_pos):
                        roulette_game.bet_position("first 12", account)
                    elif second12.collidepoint(mouse_pos):
                        roulette_game.bet_position("second 12", account)
                    elif third12.collidepoint(mouse_pos):
                        roulette_game.bet_position("third 12", account)
                    elif button_1to18.collidepoint(mouse_pos):
                        roulette_game.bet_position("1-18", account)
                    elif even.collidepoint(mouse_pos):
                        roulette_game.bet_position("even", account)
                    elif red.collidepoint(mouse_pos):
                        roulette_game.bet_position("red", account)
                    elif black.collidepoint(mouse_pos):
                        roulette_game.bet_position("black", account)
                    elif odd.collidepoint(mouse_pos):
                        roulette_game.bet_position("odd", account)
                    elif button_19to36.collidepoint(mouse_pos):
                        roulette_game.bet_position("19-36", account)
                    elif top_column_bet.collidepoint(mouse_pos):
                        roulette_game.bet_position("top 2-1", account)
                    elif middle_column_bet.collidepoint(mouse_pos):
                        roulette_game.bet_position("mid 2-1", account)
                    elif bottom_column_bet.collidepoint(mouse_pos):
                        roulette_game.bet_position("bot 2-1", account)




            # Blackjack screen events
            if current_screen == 3:
                pass

            # Account screen events
            if current_screen == 4:
                if blue_button1.collidepoint(mouse_pos):
                    account.add_twenty()
                elif blue_button2.collidepoint(mouse_pos):
                    account.add_fifty()
                elif blue_button3.collidepoint(mouse_pos):
                    account.add_hundred()

        # types and backspaces in the bet amount rectangle
        if current_screen == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    bet_text = bet_text[:-1]
                elif event.unicode.isdigit() and len(bet_text) < 2:
                    bet_text += event.unicode

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    # Colors the background
    screen.fill(WHITE)

    # Menu screen
    if current_screen == 0:
        # Displays 'GVSU Casino' title
        screen.blit(message, (200, 100))

        # Creates buttons for each game
        pygame.draw.rect(screen, BLUE, blue_button1)
        pygame.draw.rect(screen, BLUE, blue_button2)
        pygame.draw.rect(screen, BLUE, blue_button3)
        screen.blit(menu_button1_text, (blue_button1.x + 30, blue_button1.y + 10))
        screen.blit(menu_button2_text, (blue_button2.x + 30, blue_button2.y + 10))
        screen.blit(menu_button3_text, (blue_button3.x + 30, blue_button3.y + 10))

        # Account display / button
        pygame.draw.rect(screen, BLUE, balance_button)
        screen.blit(balance_button_text, (balance_button.x + 30, balance_button.y + 10))

        # Check for button clicks
        if blue_button1.collidepoint(mouse_pos) and mouse_pressed[0]:
            current_screen = 1

        if blue_button2.collidepoint(mouse_pos) and mouse_pressed[0]:
            current_screen = 2

        if blue_button3.collidepoint(mouse_pos) and mouse_pressed[0]:
            current_screen = 3

        if balance_button.collidepoint(mouse_pos) and mouse_pressed[0]:
            current_screen = 4

    # Slots screen
    elif current_screen == 1:
        screen.fill(GREEN)

        # Slots title at top of screen
        new_message = font.render("Slots", True, BLACK)
        screen.blit(new_message, (350, 0))  # Position the new message

        # Back button
        pygame.draw.rect(screen, BLUE, back_button)
        screen.blit(back_button_text, (back_button.x + 30, back_button.y + 10))

        # Account display / button
        pygame.draw.rect(screen, BLUE, balance_button)
        screen.blit(balance_button_text, (balance_button.x + 30, balance_button.y + 10))

        # bet amount rectangle
        pygame.draw.rect(screen, BLUE, bet_button, 2)
        text_surface = font.render(bet_text, True, BLACK)
        screen.blit(text_surface, (bet_button.x + 10, bet_button.y + 10))

        # place bet text
        place_bet_text = font.render('Place bet: $', True, BLACK)
        screen.blit(place_bet_text, (bet_button.x - 190, bet_button.y + 10))

        # spin button
        pygame.draw.rect(screen, BLUE, spin_button)
        spin_button_text = font.render('SPIN', True, WHITE)
        screen.blit(spin_button_text, (spin_button.x + 10, spin_button.y + 10))

        slot1 = pygame.Rect(100, 160, 100, 200)
        slot2 = pygame.Rect(225, 160, 100, 200)
        slot3 = pygame.Rect(350, 160, 100, 200)
        slot4 = pygame.Rect(475, 160, 100, 200)
        slot5 = pygame.Rect(600, 160, 100, 200)

        # Draw the rectangles

        pygame.draw.rect(screen, WHITE, slot1)
        pygame.draw.rect(screen, WHITE, slot2)
        pygame.draw.rect(screen, WHITE, slot3)
        pygame.draw.rect(screen, WHITE, slot4)
        pygame.draw.rect(screen, WHITE, slot5)

        # Border the rectangles with black

        pygame.draw.rect(screen, BLACK, slot1, 4)
        pygame.draw.rect(screen, BLACK, slot2, 4)
        pygame.draw.rect(screen, BLACK, slot3, 4)
        pygame.draw.rect(screen, BLACK, slot4, 4)
        pygame.draw.rect(screen, BLACK, slot5, 4)

        display_final_symbols()

        # make checks for bet amounts

        if spin_button.collidepoint(mouse_pos) and mouse_pressed[0]:
            if len(bet_text) >= 1 and not slots.spinning:
                invalid_bet_message = ''
                # makes sure bet is not subtracted from balance if bet is above 20
                if 0 < int(bet_text) <= 20:
                    if int(bet_text) <= account.balance:
                        invalid_bet_message = ''
                        account.place_bet(int(bet_text))
                        if not slots.spinning:
                            spin()
                        if slots.spinning:
                            slots.spinning = True
                        display_final_symbols()
                        # pygame.display.update()
                    else:
                        invalid_bet_message = 'You cannot bet more than you have!'

                else:
                    invalid_bet_message = 'Bet must be between $1 and $20!'
            else:
                invalid_bet_message = 'Please make a bet before you can spin!'

        if invalid_bet_message:
            message_surface = small_font.render(invalid_bet_message, True, BLACK)
            screen.blit(message_surface, message_rect)




    # Roulette screen
    elif current_screen == 2:
        screen.fill(GREEN)
        # Roulette title at top of screen
        new_message = font.render("Roulette", True, BLACK)
        screen.blit(new_message, (350, 0))  # Position the new message

        # Back button
        pygame.draw.rect(screen, BLUE, back_button)
        screen.blit(back_button_text, (back_button.x + 30, back_button.y + 10))

        # Account display / button
        pygame.draw.rect(screen, BLUE, balance_button)
        screen.blit(balance_button_text, (balance_button.x + 30, balance_button.y + 10))

        # Creates buttons for Board
        # Off Board Bets
        pygame.draw.rect(screen, GREEN1, first12)
        pygame.draw.rect(screen, GREEN2, second12)
        pygame.draw.rect(screen, GREEN1, third12)
        pygame.draw.rect(screen, GREEN2, button_1to18)
        pygame.draw.rect(screen, GREEN3, button_19to36)
        pygame.draw.rect(screen, GREEN3, even)
        pygame.draw.rect(screen, GREEN2, odd)
        pygame.draw.rect(screen, RED, red)
        pygame.draw.rect(screen, BLACK, black)
        screen.blit(first12_text, (first12.x + 40, first12.y + 10))
        screen.blit(second12_text, (second12.x + 20, second12.y + 10))
        screen.blit(third12_text, (third12.x + 35, third12.y + 10))
        screen.blit(button_1to18_text, (button_1to18.x + 10, button_1to18.y + 15))
        screen.blit(button_19to36_text, (button_19to36.x + 5, button_19to36.y + 15))
        screen.blit(even_text, (even.x + 7, even.y + 15))
        screen.blit(odd_text, (odd.x + 15, odd.y + 15))
        screen.blit(red_text, (red.x + 15, red.y + 15))
        screen.blit(black_text, (black.x + 7, black.y + 15))

        # Green 0
        pygame.draw.rect(screen, GREEN0, button0)
        screen.blit(button0_text, (button0.x + 20, button3.y + 65))
        # Top Row
        pygame.draw.rect(screen, RED, button3)
        pygame.draw.rect(screen, BLACK, button6)
        pygame.draw.rect(screen, RED, button9)
        pygame.draw.rect(screen, RED, button12)
        pygame.draw.rect(screen, BLACK, button15)
        pygame.draw.rect(screen, RED, button18)
        pygame.draw.rect(screen, RED, button21)
        pygame.draw.rect(screen, BLACK, button24)
        pygame.draw.rect(screen, RED, button27)
        pygame.draw.rect(screen, RED, button30)
        pygame.draw.rect(screen, BLACK, button33)
        pygame.draw.rect(screen, RED, button36)
        pygame.draw.rect(screen, GREEN2, top_column_bet)
        screen.blit(button3_text, (button3.x + 20, button3.y + 15))
        screen.blit(button6_text, (button6.x + 20, button6.y + 15))
        screen.blit(button9_text, (button9.x + 20, button9.y + 15))
        screen.blit(button12_text, (button12.x + 7, button12.y + 15))
        screen.blit(button15_text, (button15.x + 7, button15.y + 15))
        screen.blit(button18_text, (button18.x + 7, button18.y + 15))
        screen.blit(button21_text, (button21.x + 7, button21.y + 15))
        screen.blit(button24_text, (button24.x + 7, button24.y + 15))
        screen.blit(button27_text, (button27.x + 7, button27.y + 15))
        screen.blit(button30_text, (button30.x + 7, button30.y + 15))
        screen.blit(button33_text, (button33.x + 7, button33.y + 15))
        screen.blit(button36_text, (button36.x + 7, button36.y + 15))
        screen.blit(top_column_text, (top_column_bet.x + 15, top_column_bet.y + 15))

        # Middle Row
        pygame.draw.rect(screen, BLACK, button2)
        pygame.draw.rect(screen, RED, button5)
        pygame.draw.rect(screen, BLACK, button8)
        pygame.draw.rect(screen, BLACK, button11)
        pygame.draw.rect(screen, RED, button14)
        pygame.draw.rect(screen, BLACK, button17)
        pygame.draw.rect(screen, BLACK, button20)
        pygame.draw.rect(screen, RED, button23)
        pygame.draw.rect(screen, BLACK, button26)
        pygame.draw.rect(screen, BLACK, button29)
        pygame.draw.rect(screen, RED, button32)
        pygame.draw.rect(screen, BLACK, button35)
        pygame.draw.rect(screen, GREEN1, middle_column_bet)
        screen.blit(button2_text, (button2.x + 20, button2.y + 15))
        screen.blit(button5_text, (button5.x + 20, button5.y + 15))
        screen.blit(button8_text, (button8.x + 20, button8.y + 15))
        screen.blit(button11_text, (button11.x + 7, button11.y + 15))
        screen.blit(button14_text, (button14.x + 7, button14.y + 15))
        screen.blit(button17_text, (button17.x + 7, button17.y + 15))
        screen.blit(button20_text, (button20.x + 7, button20.y + 15))
        screen.blit(button23_text, (button23.x + 7, button23.y + 15))
        screen.blit(button26_text, (button26.x + 7, button26.y + 15))
        screen.blit(button29_text, (button29.x + 7, button29.y + 15))
        screen.blit(button32_text, (button32.x + 7, button32.y + 15))
        screen.blit(button35_text, (button35.x + 7, button35.y + 15))
        screen.blit(middle_column_text, (middle_column_bet.x + 15, middle_column_bet.y + 15))

        # Bottom Row
        pygame.draw.rect(screen, RED, button1)
        pygame.draw.rect(screen, BLACK, button4)
        pygame.draw.rect(screen, RED, button7)
        pygame.draw.rect(screen, BLACK, button10)
        pygame.draw.rect(screen, BLACK, button13)
        pygame.draw.rect(screen, RED, button16)
        pygame.draw.rect(screen, RED, button19)
        pygame.draw.rect(screen, BLACK, button22)
        pygame.draw.rect(screen, RED, button25)
        pygame.draw.rect(screen, BLACK, button28)
        pygame.draw.rect(screen, BLACK, button31)
        pygame.draw.rect(screen, RED, button34)
        pygame.draw.rect(screen, GREEN2, bottom_column_bet)
        screen.blit(button1_text, (button1.x + 20, button1.y + 15))
        screen.blit(button4_text, (button4.x + 20, button4.y + 15))
        screen.blit(button7_text, (button7.x + 20, button7.y + 15))
        screen.blit(button10_text, (button10.x + 7, button10.y + 15))
        screen.blit(button13_text, (button13.x + 7, button13.y + 15))
        screen.blit(button16_text, (button16.x + 7, button16.y + 15))
        screen.blit(button19_text, (button19.x + 7, button19.y + 15))
        screen.blit(button22_text, (button22.x + 7, button22.y + 15))
        screen.blit(button25_text, (button25.x + 7, button25.y + 15))
        screen.blit(button28_text, (button28.x + 7, button28.y + 15))
        screen.blit(button31_text, (button31.x + 7, button31.y + 15))
        screen.blit(button34_text, (button34.x + 7, button34.y + 15))
        screen.blit(bottom_column_text, (bottom_column_bet.x + 15, bottom_column_bet.y + 15))

        pygame.draw.circle(screen, BLACK, (150, 150), 100)

        landing_number = random.randint(0, 37)

        r_bet_x = 600
        r_bet_y = 100
        for bet in roulette_game.bets_text():
            bets_text = font.render(bet, True, WHITE)
            screen.blit(bets_text, (r_bet_x, r_bet_y))
            r_bet_y += 50


    # Blackjack screen
    elif current_screen == 3:
        card_width = 100
        card_height = 156
        dealer_card_x = 10
        dealer_card_y = 140
        player_card_x = 10
        player_card_y = 350

        # if game is None:
        screen.fill(GREEN)
        # Blackjack title at top of screen
        new_message = font.render("Blackjack", True, BLACK)
        screen.blit(new_message, (345, 5))  # Position the new message

        # Back button
        pygame.draw.rect(screen, BLUE, back_button)
        screen.blit(back_button_text, (back_button.x + 30, back_button.y + 10))

        # Account display / button
        pygame.draw.rect(screen, BLUE, balance_button)
        screen.blit(balance_button_text, (balance_button.x + 30, balance_button.y + 10))

        # Dealer title and back of cards
        dealer_title = font.render("Dealer", True, BLACK)
        screen.blit(dealer_title, (120, 100))
        pygame.draw.rect(screen, RED, (dealer_card_x, dealer_card_y, card_width, card_height))
        # pygame.draw.rect(screen, RED, (dealer_card_x + 110, dealer_card_y, card_width, card_height))

        # Your title and back of cards
        You_title = font.render("You", True, BLACK)
        screen.blit(You_title, (120, 310))
        pygame.draw.rect(screen, RED, (player_card_x, player_card_y, card_width, card_height))
        pygame.draw.rect(screen, RED, (player_card_x + 110, player_card_y, card_width, card_height))

        # Makes the three betting buttons
        pygame.draw.rect(screen, WHITE, bj_small_bet)
        pygame.draw.rect(screen, WHITE, bj_medium_bet)
        pygame.draw.rect(screen, WHITE, bj_large_bet)
        pygame.draw.rect(screen, WHITE, bj_stand)
        pygame.draw.rect(screen, WHITE, bj_hit)
        pygame.draw.rect(screen, WHITE, bj_double)
        screen.blit(small_bet_text, (bj_small_bet.x + 10, bj_small_bet.y + 10))
        screen.blit(medium_bet_text, (bj_medium_bet.x + 8, bj_medium_bet.y + 10))
        screen.blit(large_bet_text, (bj_large_bet.x + 8, bj_large_bet.y + 10))
        screen.blit(stand_text, (bj_stand.x + 30, bj_stand.y + 10))
        screen.blit(hit_text, (bj_hit.x + 30, bj_hit.y + 10))
        screen.blit(double_text, (bj_double.x + 30, bj_double.y + 10))





    # Account screen
    elif current_screen == 4:
        # Account title at top of screen
        new_message = font.render("Account", True, BLACK)
        screen.blit(new_message, (350, 0))  # Position the new message

        # Back button
        pygame.draw.rect(screen, BLUE, back_button)
        screen.blit(back_button_text, (back_button.x + 30, back_button.y + 10))

        # Displays Account Balance
        screen.blit(title_font.render(str(account), True, BLACK), (325, 100))

        # Creates buttons for each amount that can be added
        pygame.draw.rect(screen, BLUE, blue_button1)
        pygame.draw.rect(screen, BLUE, blue_button2)
        pygame.draw.rect(screen, BLUE, blue_button3)

        screen.blit(add_button1_text, (blue_button1.x + 30, blue_button1.y + 10))
        screen.blit(add_button2_text, (blue_button2.x + 30, blue_button2.y + 10))
        screen.blit(add_button3_text, (blue_button3.x + 30, blue_button3.y + 10))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
