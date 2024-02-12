import os
import pygame
import time

from sprite import Sprite
from background import Background
from level import Level
from hero import Hero
from block import Block
from utils import State, next_level_screen, game_over_screen

# GLOBAL VARIABLES
SURFACE_COLOR = (167, 255, 100)
WIDTH = 1000
HEIGHT = 1000

pygame.init()

RED = (255, 0, 0)

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Algo - 2")

font = pygame.font.SysFont(None, 24)
img = font.render('You Win', True, RED)

difficulty = 1
level = Level(difficulty)
hero = Hero() # create an instance

start_ticks = pygame.time.get_ticks() #starter tick

BackGround = Background(os.path.join(os.path.dirname(__file__), 'assets','back_ter.jpg'), [0,0])
run = True
clock = pygame.time.Clock()
screen.blit(BackGround.image, BackGround.rect)

state = State.MENU

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if state == state.MENU:
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                state = state.IN_GAME

    if state == state.IN_GAME:
        hero.handle_keys()
        screen.blit(BackGround.image, BackGround.rect)
        hero.draw(screen)

        level.update(hero)

        if hero.life <= 0:
            screen.blit(game_over_screen, (300, 300))
            state = state.LOST

        if level.done:
            screen.blit(next_level_screen, (300, 300))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    difficulty += 1
                    level = Level(difficulty)
        else:
            level.draw(screen)

    elif state == state.LOST:
        screen.blit(game_over_screen, (300, 300))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()