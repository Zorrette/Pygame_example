import pygame
import os
import random

WIDTH = 800
HEIGHT = 800


class Block(pygame.sprite.Sprite):
	image =  pygame.image.load(os.path.join(os.path.dirname(__file__), 'assets','new_crystal.png'))

	def __init__(self,):
		pygame.sprite.Sprite.__init__(self)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = random.randrange(WIDTH - self.rect.width * 3), random.randrange(HEIGHT - self.rect.height * 3)

	def draw(self, surface):
		""" Draw on surface """
		surface.blit(self.image, (self.rect.left, self.rect.top))

class Spike(pygame.sprite.Sprite):
	image =  pygame.image.load(os.path.join(os.path.dirname(__file__), 'assets','spike.png'))

	def __init__(self,):
		pygame.sprite.Sprite.__init__(self)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = random.randrange(WIDTH - self.rect.width * 3), random.randrange(HEIGHT - self.rect.height * 3)

	def draw(self, surface):
		""" Draw on surface """
		surface.blit(self.image, (self.rect.left, self.rect.top))