import pygame
import os

class Hero(object):  # represents the bird, not the game
    def __init__(self):
        """ The constructor of the class """
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), 'assets','moi_min.png'))
        self.rect = self.image.get_rect()

        # the default's position
        self.rect.x = 0
        self.rect.y = 0

        self.life = 3

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 5 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]: # down key
            self.rect.y += dist # move down
        elif key[pygame.K_UP]: # up key
            self.rect.y -= dist # move up
        if key[pygame.K_RIGHT]: # right key
            self.rect.x += dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.rect.x -= dist # move left

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.rect.x, self.rect.y))