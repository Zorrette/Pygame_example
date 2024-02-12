from enum import Enum
import pygame
import os

class State(Enum):
    MENU = 'menu'
    IN_GAME = 'in_game'
    LOST = 'lost'

next_level_screen = pygame.image.load(os.path.join(os.path.dirname(__file__), 'assets','next_lvl.png'))

game_over_screen = pygame.image.load(os.path.join(os.path.dirname(__file__), 'assets','loser.png'))
