import os
import pygame
import random
from sprite import Sprite
from background import Background
from hero import Hero
from block import Block

# GLOBAL VARIABLES
SURFACE_COLOR = (167, 255, 100)
WIDTH = 1000
HEIGHT = 1000

pygame.init()

RED = (255, 0, 0)

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Algo - 2")

level_blocks = []
level_blocks.append(Block([random.randrange(WIDTH), random.randrange(HEIGHT)]))

# block = 
hero = Hero() # create an instance
start_ticks = pygame.time.get_ticks() #starter tick
BackGround = Background(os.path.join(os.path.dirname(__file__), 'assets','back_ter.jpg'), [0,0])
exit = True
clock = pygame.time.Clock()
screen.blit(BackGround.image, BackGround.rect)

while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
            pygame.quit()

    hero.handle_keys()
    screen.blit(BackGround.image, BackGround.rect)
    hero.draw(screen)
    for block in level_blocks:
        block.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()