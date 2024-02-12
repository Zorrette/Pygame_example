import pygame
from block import Block, Spike

class Level(object):  # handle the state of the game
    def __init__(self, level=1):
        self.done = False
        self.level = level
        self.level_blocks = pygame.sprite.Group()
        self.level_spikes = pygame.sprite.Group()

        for i in range(level):
            self.level_blocks.add(Block())

        if level > 2:
            for i in range(level - 2):
                self.level_spikes.add(Spike())

    def update(self, hero):
        eaten = pygame.sprite.spritecollide(hero, self.level_blocks, True)
        eaten = pygame.sprite.spritecollide(hero, self.level_spikes, False)
        if len(eaten):
            hero.life = hero.life - 1

        if len(self.level_blocks) == 0:
            self.done = True

    def draw(self, screen):
        self.level_blocks.draw(screen)
        self.level_spikes.draw(screen)