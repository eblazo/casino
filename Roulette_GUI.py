import random
import time
import pygame
import Roulette_Board
import sys
from account import Account

# Initialize Pygame
pygame.init()

# Set up the window dimensions
width, height = 800, 600

# Create the window
screen = pygame.display.set_mode((width, height))

# used colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 50, 160)
GREEN = (0, 100, 0)
GREEN0 = (0, 255, 0)
RED = (255, 0, 0)

# board label font
font = pygame.font.SysFont(None, 25)
title_font = pygame.font.SysFont(None, 96)

# Board Variables
board = []
number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'
               '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'
               '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36']
for i in range(0, 37):
    board.append(i)
red = [1, 3, 5, 7, 9, 12, 14, 16, 18,
       19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17,
         20, 22, 24, 26, 28, 29, 31, 33, 35]
columnA = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
columnB = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
columnC = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]

# button size and placement
top_column = []
middle_column = []
bottom_column = []
button_width, button_height = 50, 50


def roulette(money):

    # Title
    small_font = pygame.font.SysFont(None, 36)
    back_button = pygame.Rect(0, 0, 120, 40)
    back_button_text = small_font.render("Back", True, WHITE)
    new_message = title_font.render("Roulette", True, BLACK)
    screen.blit(new_message, (350, 0))  # Position the new message

    # Create Balance Button
    balance_button = pygame.Rect(680, 0, 120, 40)
    balance_button_text = small_font.render(str(money), True, WHITE)

    # Colors the background
    screen.fill(GREEN)

    # Account
    pygame.draw.rect(screen, BLUE, balance_button)
    screen.blit(balance_button_text, (balance_button.x + 30, balance_button.y + 10))

    # Back Button
    pygame.draw.rect(screen, BLUE, back_button)
    screen.blit(back_button_text, (back_button.x + 30, back_button.y + 10))

    # Generates board
    Roulette_Board.create_board()

    

