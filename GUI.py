import pygame
import sys
from account import Account

# Initialize Pygame
pygame.init()

account = Account()

# Set up the window dimensions
width, height = 800, 600

# Create the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Casino')

# Creates default colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 50, 160)

# Create font
font = pygame.font.SysFont(None, 48)
title_font = pygame.font.SysFont(None, 96)
small_font = pygame.font.SysFont(None, 36)

# Create displayed message
message = title_font.render("GVSU Casino", True, BLACK)

# Create buttons for menu and account screens
button_width, button_height = 200, 50
button1 = pygame.Rect(300, 200, button_width, button_height)
button2 = pygame.Rect(300, 300, button_width, button_height)
button3 = pygame.Rect(300, 400, button_width, button_height)

# Creates text for menu screen buttons
button1_text = font.render("Slots", True, WHITE)
button2_text = font.render("Roulette", True, WHITE)
button3_text = font.render("Blackjack", True, WHITE)

# Creates text for adding money to account
add_button1_text = font.render("$20", True, WHITE)
add_button2_text = font.render("$50", True, WHITE)
add_button3_text = font.render("$100", True, WHITE)

# Creates back button
back_button = pygame.Rect(0, 0, 120, 40)
back_button_text = small_font.render("Back", True, WHITE)

# Sets current screen to menu
current_screen = 0

# Main loop
running = True
while running:
    # Creates balance button
    balance_button = pygame.Rect(680, 0, 120, 40)
    balance_button_text = small_font.render(str(account), True, WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if button1.collidepoint(mouse_pos) and current_screen == 4:
                    account.add_twenty()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if button2.collidepoint(mouse_pos) and current_screen == 4:
                    account.add_fifty()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if button3.collidepoint(mouse_pos) and current_screen == 4:
                    account.add_hundred()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if back_button.collidepoint(mouse_pos):
                    current_screen = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if balance_button.collidepoint(mouse_pos):
                    current_screen = 4

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    # Colors the background
    screen.fill(WHITE)

    # Menu screen
    if current_screen == 0:
        # Displays 'GVSU Casino' title
        screen.blit(message, (200, 100))

        # Creates buttons for each game
        pygame.draw.rect(screen, BLUE, button1)
        pygame.draw.rect(screen, BLUE, button2)
        pygame.draw.rect(screen, BLUE, button3)
        screen.blit(button1_text, (button1.x + 30, button1.y + 10))
        screen.blit(button2_text, (button2.x + 30, button2.y + 10))
        screen.blit(button3_text, (button3.x + 30, button3.y + 10))

        # Account display / button
        pygame.draw.rect(screen, BLUE, balance_button)
        screen.blit(balance_button_text, (balance_button.x + 30, balance_button.y + 10))

        # Check for button clicks
        if button1.collidepoint(mouse_pos) and mouse_pressed[0]:
            current_screen = 1

        if button2.collidepoint(mouse_pos) and mouse_pressed[0]:
            current_screen = 2

        if button3.collidepoint(mouse_pos) and mouse_pressed[0]:
            current_screen = 3

        if balance_button.collidepoint(mouse_pos) and mouse_pressed[0]:
            current_screen = 4

    # Slots screen
    elif current_screen == 1:
        # Slots title at top of screen
        new_message = font.render("Slots", True, BLACK)
        screen.blit(new_message, (350, 0))  # Position the new message

        # Back button
        pygame.draw.rect(screen, BLUE, back_button)
        screen.blit(back_button_text, (back_button.x + 30, back_button.y + 10))

        # Account display / button
        pygame.draw.rect(screen, BLUE, balance_button)
        screen.blit(balance_button_text, (balance_button.x + 30, balance_button.y + 10))

    # Roulette screen
    elif current_screen == 2:
        # Roulette title at top of screen
        new_message = font.render("Roulette", True, BLACK)
        screen.blit(new_message, (350, 0))  # Position the new message

        # Back button
        pygame.draw.rect(screen, BLUE, back_button)
        screen.blit(back_button_text, (back_button.x + 30, back_button.y + 10))

        # Account display / button
        pygame.draw.rect(screen, BLUE, balance_button)
        screen.blit(balance_button_text, (balance_button.x + 30, balance_button.y + 10))

    # Blackjack screen
    elif current_screen == 3:
        # Blackjack title at top of screen
        new_message = font.render("Blackjack", True, BLACK)
        screen.blit(new_message, (350, 0))  # Position the new message

        # Back button
        pygame.draw.rect(screen, BLUE, back_button)
        screen.blit(back_button_text, (back_button.x + 30, back_button.y + 10))

        # Account display / button
        pygame.draw.rect(screen, BLUE, balance_button)
        screen.blit(balance_button_text, (balance_button.x + 30, balance_button.y + 10))

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
        pygame.draw.rect(screen, BLUE, button1)
        pygame.draw.rect(screen, BLUE, button2)
        pygame.draw.rect(screen, BLUE, button3)

        screen.blit(add_button1_text, (button1.x + 30, button1.y + 10))
        screen.blit(add_button2_text, (button2.x + 30, button2.y + 10))
        screen.blit(add_button3_text, (button3.x + 30, button3.y + 10))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()